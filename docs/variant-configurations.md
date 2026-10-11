# Population configurations

| Item | 200 W | 2 kW |
|---|---|---|
| D1/D2 | BAT42W, SOD-123 footprint | BAT42W, SOD-123 footprint |
| R1/R2/R4/R5 | 150 ohm | 100 ohm |
| R3/R6 | 56 ohm | 100 ohm |
| R7/R11 | 3.3 kohm | 3.9 kohm |
| R8/R12 | 1.6 kohm | 1.2 kohm |
| R23 | 2.7 kohm | 2.7 kohm |
| C1/C2 | 0.01 uF | 0.01 uF (10 nF) |
| T1/T2 notation | 1:16T | 1:24T |
| #43 cores per transformer / PCB | 1 / 2 | 2 / 4 |

The 1:16T and 1:24T notation is preserved as recorded; it is not independently
reinterpreted as a turns ratio. Other electrical values remain those of the curated
schematics.

J4 assignments: 1 +3.3 V; 2 FWD; 3 REF; 4 INT; 5 GND. Both circuits use the same
detector/divider, interrupt-selection and frequency-divider connections. The preserved
cascaded divider uses inverted outputs and is documented as divide by four.

Historical jumper note: both JP1 and JP2 at 1-2 select SWR interrupt (noted fixed 3:1);
both at 2-3 select power interrupt with VR1 threshold adjustment. This retains the
engineering note; it is not a new verification of threshold accuracy.

H1-H4 explicitly represent the existing grounded holes; no additional holes or electrical
nets were created. Common PCB footprint values describe the default 200 W population and
are not a 2 kW purchasing BOM.
