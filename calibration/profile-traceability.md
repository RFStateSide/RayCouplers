# Calibration provenance

The two measurement workbooks in measurements/ are byte-for-byte copies of the supplied originals. Neither was edited. RayPowerMeter source was consulted for traceability and remains unchanged.

| Firmware profile | Workbook source | Evidence |
|---|---|---|
| kCalProfile200W_Fwd_v1 | RayCoupler200_WtoV.xlsx, Sheet2 A2:B20 | All 19 forward voltage/power pairs match; recorded range 0.1–250 W |
| kCalProfile200W_Ref_v1 | No independently identified reflected measurement column | Forward voltages multiplied by 1.15 at unchanged watts; owner confirms experimental adjustment |
| kCalProfile2KW_Fwd_v1 | RayCoupler2000_WtoV.xlsx, Sheet1 M4:N17; divider label M2 | All 14 pairs through 1500 W match; selected divider 3.9k/1.2k |
| kCalProfile2KW_Ref_v1 | Same numerical values as forward array | No independent reflected measurement verification established |

The active 2 kW 2500 W/2.820 V endpoint is estimated. Its selected workbook ADC cell is blank. The commented 2000 W/2.530 V estimate is not active. Other workbook columns preserve earlier curves and should not be conflated with the selected profile.

BAT42W detector identity, the divider populations and core configurations are owner-confirmed. The workbooks do not independently establish tested detector manufacturer, exact winding construction or all frequency/instrument/temperature conditions.

The 1.15 multiplier is experimental, not a verified universal correction. The derived reflected endpoint is 3.450 V at 250 W and its usable ADC range is unverified. Historical curves are not guaranteed calibration for a new board.

## Deferred RayPowerMeter work

Current firmware preferences allow 20 points, but RfPowerSensor runtime retains only 15. The 19-point 200 W factory profile is truncated at its 125 W point and table conversion clamps higher voltages there. This is a mandatory future RayPowerMeter release correction.

Current factory selection copies the forward array into both paths; separate reflected arrays are not selected. Desktop/serial calibration limits and raw/smoothed calculation consistency also need end-to-end review. The software release is intended to retain measured baseline tables and remove unsupported experimental adjustments. No software changes or builds were performed in Phase 2.

## Phase 3 distribution preparation

Original workbooks remain unchanged in the excluded local evidence area. Personal creator/last-modifier metadata requires owner selection. [200 W measured forward CSV](reference/200w-measured-forward.csv) preserves the 19 Sheet2 B(voltage)/A(power) pairs; [2 kW measured forward CSV](reference/2kw-measured-forward.csv) preserves the 14 Sheet1 N(voltage)/M(power) pairs. Each row records the source cells. No estimated endpoint or reflected 1.15 experiment is inserted into measured exports. These excerpts do not replace the full private experiment history.

Fair-Rite 5943001401 and 21 AWG high-temperature enameled wire are now owner-confirmed construction facts. That does not establish missing test conditions or independent reflected measurements. RayPowerMeter source/Git state remain unchanged; software corrections are deferred.
