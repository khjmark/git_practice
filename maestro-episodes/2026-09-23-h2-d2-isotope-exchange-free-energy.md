---
task: unsupported
engine: none
error_class: support_gap
outcome: support_gap
---
Symptom: The user requested a Gibbs free-energy calculation for the isotope-exchange reaction H2 + D2 -> 2 HD.

Attempts: The live capability catalog was searched for "free energy", "thermochemistry", "reaction energy", "reaction free energy", "Gibbs", "isotope", "deuterium", and the user's Korean wording. ThermoTask can optimize one molecular system and compute its thermochemistry. IsotopeShiftTask accepts isotope substitutions but produces only isotope_frequencies. ReactionBarrierTask produces reaction_free_energy, but describes an elementary-reaction path between distinct minima and does not provide isotope-resolved thermochemistry for this exchange.

Result: No single supported MAESTRO task can calculate the requested isotope-exchange Gibbs free energy. No calculation was run.

Context: The missing capability is thermochemistry with explicit isotope masses, combined stoichiometrically across H2, D2, and HD to obtain a reaction Gibbs free energy at a specified temperature and standard state.
