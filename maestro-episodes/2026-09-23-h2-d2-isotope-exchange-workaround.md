---
task: unsupported
engine: none
error_class: support_gap
outcome: workaround
wall_time_s: 0.4
method: rigid-rotor/anharmonic-oscillator
cores: 1
mode: local
---
Symptom: MAESTRO has no task that combines explicit isotope masses with molecular thermochemistry and a stoichiometric reaction free energy for H2 + D2 -> 2 HD.

Attempts: A direct ideal-gas statistical-thermodynamics calculation was written after the user accepted 298.15 K and 1 bar. It used experimental omega_e, omega_e*x_e, omega_e*y_e, B_e, and alpha_e constants; direct rigid-rotor sums; anharmonic zero-point energies; molecular symmetry numbers; and translational mass factors.

Result: The workaround completed successfully. At 298.15 K it gave Kp = 3.257825 and Delta_r G degrees = -2.927797 kJ/mol. The equilibrium constant agrees with the literature value 3.26 at 25 degrees C.

Context: Ideal gas and equilibrium ortho/para populations were assumed. The 1 bar standard-state factor cancels because the reaction has zero change in gas molecule count. The calculation script is h2_d2_hd_gibbs.py.
