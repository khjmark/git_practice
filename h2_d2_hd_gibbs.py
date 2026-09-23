"""Ideal-gas isotope-exchange thermodynamics for H2 + D2 -> 2 HD.

The model uses a rigid-rotor/anharmonic-oscillator partition function,
experimental spectroscopic constants, and equilibrium nuclear-spin statistics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log


R = 8.31446261815324  # J mol^-1 K^-1
HC_OVER_K = 1.438776877  # K cm


@dataclass(frozen=True)
class Isotopologue:
    mass_u: float
    omega_e: float
    omega_exe: float
    omega_eye: float
    b_e: float
    alpha_e: float
    symmetry_number: int

    @property
    def vibrational_zero_point_cm(self) -> float:
        return self.omega_e / 2 - self.omega_exe / 4 + self.omega_eye / 8

    @property
    def b_0(self) -> float:
        return self.b_e - self.alpha_e / 2


SPECIES = {
    "H2": Isotopologue(2.01565006446, 4401.213, 121.336, 0.8129, 60.853, 3.0622, 2),
    "D2": Isotopologue(4.02820355624, 3115.5, 61.82, 0.562, 30.4436, 1.0786, 2),
    "HD": Isotopologue(3.02192681035, 3813.15, 91.65, 0.723, 45.655, 1.986, 1),
}


def rotational_partition(species: Isotopologue, temperature: float) -> float:
    """Direct rigid-rotor sum, with the molecular symmetry number."""
    total = 0.0
    for j in range(200):
        term = (2 * j + 1) * exp(-HC_OVER_K * species.b_0 * j * (j + 1) / temperature)
        total += term
        if j > 20 and term < 1e-15 * total:
            break
    return total / species.symmetry_number


def vibrational_partition(species: Isotopologue, temperature: float) -> float:
    """Ground-state-referenced oscillator partition function including ZPE."""
    zpe_k = HC_OVER_K * species.vibrational_zero_point_cm
    fundamental_cm = species.omega_e - 2 * species.omega_exe + 3.25 * species.omega_eye
    theta_v = HC_OVER_K * fundamental_cm
    return exp(-zpe_k / temperature) / (1 - exp(-theta_v / temperature))


def calculate(temperature: float = 298.15) -> tuple[float, float]:
    q_rot = {name: rotational_partition(sp, temperature) for name, sp in SPECIES.items()}
    q_vib = {name: vibrational_partition(sp, temperature) for name, sp in SPECIES.items()}

    # Translational V factors cancel because delta(nu) = 0.
    translational_ratio = (
        SPECIES["HD"].mass_u**3
        / (SPECIES["H2"].mass_u * SPECIES["D2"].mass_u) ** 1.5
    )
    internal_ratio = (q_rot["HD"] * q_vib["HD"]) ** 2 / (
        q_rot["H2"] * q_vib["H2"] * q_rot["D2"] * q_vib["D2"]
    )
    equilibrium_constant = translational_ratio * internal_ratio
    delta_g_j_mol = -R * temperature * log(equilibrium_constant)
    return equilibrium_constant, delta_g_j_mol


if __name__ == "__main__":
    T = 298.15
    Kp, delta_g = calculate(T)
    print(f"T = {T:.2f} K")
    print("standard state = ideal gas, 1 bar")
    print(f"Kp = {Kp:.6f}")
    print(f"Delta_r G° = {delta_g / 1000:.6f} kJ mol^-1")
