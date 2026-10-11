# 2 kW population assembly

Use [common assembly instructions](common.md) and [the 2 kW
BOM](../../bom/2kw/RayCoupler-2kw-population.csv).

Variant checks: R1–R6 100 ohm; R7/R11 3.9k; R8/R12 1.2k. D1/D2 BAT42W; C1/C2 10 nF; R23
2.7k. All remaining values come from the matching curated schematic.

Each T1/T2 has 24 turns of 21 AWG high-temperature enameled copper wire. Use two taped
Fair-Rite 5943001401 #43 toroids per transformer, 4 cores total per PCB. See [construction
evidence and unresolved lead mapping](../transformer-construction.md).

Review all reference designators against the selected schematic; the common PCB's
component value fields describe the default 200 W population and do not select the 2 kW
parts. Hand assembly uses the BOM and native placement drawing together. No automated
pick-and-place package has been validated.

Historical measured forward evidence contains 14 points through 1500 W. The active 2500 W
firmware endpoint is estimated, and the 2000 W estimate was commented out. Establish
calibration for the actual completed system; see [calibration
provenance](../../calibration/profile-traceability.md).
