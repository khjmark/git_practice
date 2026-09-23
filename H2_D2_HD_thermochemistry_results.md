# H₂ + D₂ → 2HD thermochemistry

## Conditions

- Temperature: 298.15 K
- Standard pressure: 1 bar
- Phase/model: ideal gas
- Execution: Slurm job `14066` on `32core_partition`
- Method: translational partition function, direct rigid-rotor sum, and anharmonic-oscillator spectroscopic model
- Energy unit: kJ mol⁻¹
- Entropy unit: J mol⁻¹ K⁻¹

The reaction column is calculated as

\[
\Delta_r X = 2X(\mathrm{HD})-X(\mathrm{H_2})-X(\mathrm{D_2}).
\]

## Component-resolved results

| Quantity | H₂ | D₂ | HD | Reaction |
|---|---:|---:|---:|---:|
| ZPE | 25.963440 | 18.450786 | 22.534689 | +0.655151 |
| \(U_\mathrm{trans}\) | 3.718436 | 3.718436 | 3.718436 | 0.000000 |
| \(U_\mathrm{rot}\) | 2.237317 | 2.358497 | 2.298070 | +0.000327 |
| \(U_\mathrm{vib,thermal}\) | 0.000000 | 0.000019 | 0.000001 | −0.000017 |
| \(U_\mathrm{vib,total}\) | 25.963440 | 18.450805 | 22.534690 | +0.655134 |
| \(U_\mathrm{electronic}\) | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| \(U_\mathrm{total}\) | 31.919193 | 24.527737 | 28.551196 | **+0.655461** |
| \(PV\) | 2.478957 | 2.478957 | 2.478957 | **0.000000** |
| \(H=U+PV\) | 34.398150 | 27.006694 | 31.030153 | **+0.655461** |
| \(S\) | 130.539605 | 144.876828 | 143.717370 | **+12.018306** |
| \(TS\) | 38.920383 | 43.195026 | 42.849334 | **+3.583258** |
| \(G=H-TS\) | −4.522234 | −16.188332 | −11.819181 | **−2.927797** |

## Gibbs free energy and equilibrium constant

\[
\Delta_r G^\circ
=\Delta_r H^\circ-T\Delta_r S^\circ
=0.655461-3.583258
=\boxed{-2.927797\ \mathrm{kJ\,mol^{-1}}}.
\]

\[
K_p=\exp\left(-\frac{\Delta_rG^\circ}{RT}\right)
=\boxed{3.257825}.
\]

The negative reaction Gibbs free energy means that HD formation is favored under the stated standard conditions.

## Notes

- The common nondegenerate electronic ground-state minimum is used as the zero of electronic energy. Consequently, the electronic contribution cancels for this isotope-exchange reaction.
- Because the reaction has \(\Delta n_\mathrm{gas}=0\), the reaction-level \(PV\) contribution is zero.
- Spectroscopic constants were taken from the [NIST Computational Chemistry Comparison and Benchmark Database](https://cccbdb.nist.gov/expdiatomicsx.asp).
- The computed \(K_p\) agrees with the reported room-temperature value of approximately 3.26.
