# Phase 3 engineering validation

Preparation identifier: P3-prep-01. KiCad CLI 9.0.7. This is an engineering-checked preliminary package, not physical fabrication/test acceptance. Source authority remains hardware/common/RayCouplers.kicad_pcb, with common 200 W and separate 2 kW schematic populations.

## CAD, geometry and population

| Check | Common PCB | 200 W paired project | 2 kW paired project |
|---|---:|---:|---:|
| DRC errors / warnings | 0 / 48 | 0 / 48 | 0 / 48 |
| Unconnected / parity issues | 0 / 0 | 0 / 0 | 0 / 0 |
| ERC errors / warnings | — | 4 / 6 | 4 / 14 |

Counts match the accepted Phase 2 baseline. DRC warnings: 37 library footprint comparisons, six missing courtyards, two text-height findings, one diode reference mask-clipping finding and two diode-area reference overlaps. ERC errors remain two undriven externally supplied power-input nets and two intentionally unused U21 complementary outputs. Symbol comparison warnings remain six/fourteen. No checks were suppressed and no circuit rewiring or automatic footprint modernization was performed. The Phase 2 [exception rationale](validation.md) remains applicable.

All 200 segments, 214 vias, 54 footprint placements/pads/graphics, original board text, outline/openings, and zone definitions compare unchanged. Zone refill was performed after stackup metadata changes. Netlists retain all 30 named nets and 50 original electrical/test-point references; H1–H4 remain on existing GND. Both 50-reference BOMs pass value, footprint, quantity and variant-difference checks. Core procurement is two/four; each custom transformer is 16/24 turns with confirmed wire/core metadata. Source notices are file/title metadata and do not alter on-board artwork.

During metadata preparation, an encoding error was caught by validation and the exact affected values/text were restored from the accepted baseline. The final text/graphics equality and CAD results above confirm its resolution before packaging.

## Fabrication rules and native stackup

Copper metadata is now nominal 70 micrometres each side, dielectric 1.440 mm, mask 0.010 mm each side, total nominal 1.6 mm, FR-4 TG150, blue/white and leaded HASL. The source routing and project DRC rules are retained. Those metadata changes do not change exported CAM geometry.

A separate disposable 8 mil (0.2032 mm) rule check found 14 pre-existing clearance gaps about 0.2010–0.2025 mm. There are no track-width violations in that check. The source has 0.2 mm netclass clearance. Do not characterize the design as strict 8 mil spacing compliant. [Fabrication notes](fabrication.md) require fabricator acceptance of the actual clearance geometry with 2 oz copper before ordering. This is an additional constraint comparison, not a new DRC regression under accepted project rules. Missing local library tables in that disposable rule-only diagnostic also produced library-resolution warnings; normal project checks above use the proper local tables.

## CAM package

Nine Gerbers parse with the standard-library KiCad-subset checker: absolute metric 4.6 coordinates, aperture definitions/macros, dark/clear polarity, regions and linear/circular interpolation. Unsupported drawing commands are rejected; this checker is not a general CAM engine. Diode copper/mask/paste flashes match 1.2 × 1.2 mm SOD-123 pads, 3.3 mm centers, pin 1 K/pin 2 A. Native cathode marking/pad rotation is preserved. Both mask layers contain no separate via-center opening flashes; tenting is retained.

Edge.Cuts has three closed four-edge rectangles: 70 × 102 mm outside and two 20 × 30 mm routed openings. Four grounded plated 3.2 mm mounting hits remain. Excellon inventory: 244 plated hits and zero non-plated hits/slots. The empty NPTH file/map is intentional; openings are routed, not drilled. Drill diameters/counts: 0.300/12, 0.500/202, 0.710/3, 0.750/6, 1.000/12, 1.100/5, 3.200/4 (mm/count).

B.Paste intentionally has two 6 × 6 mm grounded T1/T2 pin-5 apertures; it is not empty. The front assembly population remains controlled by its BOM. No automated placement/assembly package was claimed or generated.

All nine Gerber primitive inventories are identical to same-setting diagnostic exports of the accepted Phase 2 board. The ZIP has exactly 19 members, matches every loose payload byte and passes CRC/SHA-256 checks. manifest.json records source SHA-256, KiCad version and explicit settings. SHA256SUMS.txt includes the ZIP. The job's automatic 70.05 × 102.05 mm stroked bounds are replaced with nominal centerline dimensions and its controlled preparation identifier. No historical ZIP was overwritten.

## Historical January comparison

All 244 plated hits match the retained January order package within 0.002 mm unit-rounding tolerance. Back copper/mask/paste/legend and Edge.Cuts primitive inventories match exactly. Front mask/paste each replace four historical detector flashes with SOD-123 geometry and wider center spacing. Front copper replaces four detector flashes and three regenerated zone polygons (537 other primitives shared). Zone contour differences include fill-engine/clearance changes; this is not a claim of byte-identical historical fills. Native tracks/vias and accepted Phase 2 fills are preserved.

Front legend shares 2320 primitives, with 59 historical-only and 52 release-only primitives, comprising four mask-subtraction pad flashes plus line changes. Retained detector outline/reference placement and current mask clipping account for material changes around the revised detector footprint and nearby labels. Ordinary unchanged back legend remains exact. Silkscreen overlaps are disclosed, not claimed resolved.

## Portability, preservation and review

Both schematic PDF previews and the common board preview were visually inspected; notices fit the title area, and accepted placement/annotations remain readable with retained fine-board-label limitations. The historical photograph was visually identified and copied unchanged. Original hardware directories, calibration workbooks, preserved archives, RayPowerMeter files and its existing Git status/HEAD remain unchanged by SHA-256/status checks. No firmware builds, hardware operations, orders, Git initialization/commit/push, GitHub actions or publication occurred.

A diagnostics-only copy of the proposed tracked tree passed CAD/BOM portable validation and manufacturing package integrity checks without original Windows directories, private archives or original Excel files. Selected text patterns show no owner-specific paths, personal identifiers or credential signatures. This focused scan does not replace final human selection/provenance/legal review. [Repository inventory](repository-inventory.csv) and [asset review](asset-provenance.md) identify those remaining decisions. Diagnostic JSON/log/PDF/PNG files stay in ignored validation/; none are included in the manufacturer ZIP.
