# Calibration reference and traceability

The repository distributes measured-data CSV excerpts from the original
RayCoupler measurement workbooks. The workbooks are retained privately and were
not edited during source preparation. CSV rows identify their source cells;
the excerpts do not replace the full experimental history.

## Recorded measurements

| Historical profile | Workbook source | Evidence |
|---|---|---|
| kCalProfile200W_Fwd_v1 | RayCoupler200_WtoV.xlsx, Sheet2 A2:B20 | 19 pairs, 0.1–250 W |
| kCalProfile200W_Ref_v1 | No independently identified reflected measurement column | Forward voltages multiplied by 1.15 at unchanged watts |
| kCalProfile2KW_Fwd_v1 | RayCoupler2000_WtoV.xlsx, Sheet1 M4:N17; divider label M2 | 14 pairs through 1500 W; selected divider 3.9k/1.2k |
| kCalProfile2KW_Ref_v1 | Same values as historical forward array | No independent reflected measurement verification |

The [200 W forward CSV](reference/200w-measured-forward.csv) preserves Sheet2
B(voltage)/A(power) pairs. The [2 kW forward CSV](reference/2kw-measured-forward.csv)
preserves Sheet1 N(voltage)/M(power) pairs. No estimated endpoints or reflected
adjustments are inserted into these measured exports.

BAT42W, divider populations and core configurations are established project
facts. The workbooks do not establish the exact tested diode manufacturer or all
winding, frequency, instrument and temperature conditions.

## Estimates and reflected experiments

The historical 2 kW firmware endpoint of 2500 W / 2.820 V was estimated; its
selected workbook ADC cell is blank. The older 2000 W / 2.530 V estimate was
commented out and was not active. Other workbook columns contain earlier curves,
which must not be conflated with the selected profile.

The 200 W reflected 1.15 multiplier was experimental, not a verified universal
correction. Its derived endpoint is 3.450 V at 250 W; usable ADC range is
unverified. Identical historical 2 kW forward/reflected arrays do not establish
an independently measured reflected calibration.

## RayPowerMeter integration evidence

The following findings describe the RayPowerMeter source snapshot examined
during repository preparation on 2026-10-10. They are dated findings, not claims
about every subsequent firmware revision.

Preferences allow 20 calibration points, while RfPowerSensor runtime retains
15. The 19-point 200 W factory profile is truncated at its 125 W point, and table
conversion clamps higher voltages at that endpoint. Factory selection copies
the forward array into both paths rather than selecting the separate reflected
arrays.

Desktop/serial limits and raw/smoothed calculation consistency also require
system-level verification. These software observations affect how historical
tables are used; they do not change the underlying measured CSV evidence.
RayPowerMeter corrections and firmware acceptance belong to that separate
project. No software changes are supplied here.

## Applying the reference

Each new system requires appropriate calibration and verification across its
intended operating conditions. Historical curves, estimates and experimental
adjustments are not guaranteed calibration for another assembly.

Use the matching population and [transformer construction](../docs/transformer-construction.md).
Established materials do not resolve missing test conditions or reflected
measurements. See [known limitations](../docs/known-limitations.md) and the
[engineering audit](../PUBLIC_RELEASE_AUDIT.md) for the evidence boundaries.
