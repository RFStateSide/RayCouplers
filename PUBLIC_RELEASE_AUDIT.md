# RayCouplers — Public Release Engineering Audit

## Scope and Authorship

Prepared with OpenAI Codex. Reviewed by RF StateSide LLC. This report consolidates
engineering evidence from the common-PCB and manufacturing preparation records,
with separately attributed RF StateSide test reports. It is not an independent
laboratory certification.

Record date: 2026-10-11. Historical automated results below are preserved evidence,
not newly executed full CAD checks. The completed document has not yet received
RF StateSide review attribution.

## Audited Repository Revision

The documentation work starts from main at:

```text
73ce330b5b8a8c7fac3e1bf58c9b55848f149559
```

That committed baseline contains 82 tracked files. The documentation revision
containing this report is initially an uncommitted working-tree revision, not a
new clean-cloned GitHub commit.

Original evidence remains recoverable at the baseline revision in
docs/validation.md and docs/phase3-validation.md. Internal readiness, selection
inventory and website-handoff records also remain in earlier Git history.
Their removal from the current tree does not erase history.

## Historical Hardware and Supplied Design

RF StateSide reports fabrication, manual SMT population/reflow and testing of
both historical configurations with RayPowerMeter and RayRailSwSense. Private
PCBWay production evidence includes the January 3, 2026 order artifacts,
forty-board production and 2 × 2 supplier panelization.

January fabrication used SOD-323 detector pads and four grounded holes.
The supplied SOD-123 common board follows the later historical 200 W geometry;
the historical 2 kW native PCB lacked the four mounting footprints.
P3-prep-01 is not an identical January revision and has not been physically
fabricated and tested.

Early 2 kW experiments used 1N4148 before BAT42W selection for improved low-power
response. Physical inspection established BAT42W, R23 = 2.7 kΩ and C1/C2 = 10 nF
on the 2 kW hardware. Stale BAT15-03W/purchasing records are not the supplied
population authority. Old/new annotations remain in
[annotation-history.json](docs/annotation-history.json).

## Common PCB and Population Consolidation

There is one editable common PCB with 200 track segments, 214 vias, 54 footprint
placements, a 70 × 102 mm outline and two 20 × 30 mm routed openings.
Four plated grounded 3.2 mm holes remain at (72,91), (72,185), (128,91) and
(128,185) mm.

Comparisons preserved tracks, vias, placements, pads, footprint lines/arcs,
board text, outline/openings, zone definitions, clearances and keepouts.
Zones were refilled and saved; the stale D2 clearance finding was removed.

Both netlists retain 30 named nets and 50 original electrical/test-point
references. Added H1–H4 represent existing mounting pads on GND, not new circuit
nets. J4 remains 1 +3.3 V, 2 FWD, 3 REF, 4 INT, 5 GND.

D1/D2 retain 1.2 × 1.2 mm SOD-123 pads at 3.3 mm centers, pad 1 K/pad 2 A.
Copper, mask and paste geometry agree. The local X = -2.36 mm closed vertical
silkscreen edge marks the cathode. D2 cathode is left in board coordinates;
D1 is rotated 180° with cathode right.

The two population BOMs each cover 48 soldered/assembled components and two
PCB test points, plus separate board-feature/accessory/material requirements.
Twelve variant value differences were checked. Core procurement is two per
200 W board and four per 2 kW board; turns are 16/24 using the established core
and wire recipe.

## Significant Engineering Findings

Mounting references were made unique and represented schematically to resolve
extra-footprint/parity findings. J4 footprint naming and jumper inclusion were
aligned. Footprint filters accept retained packages.

Legacy 2 kW symbol-cache aliases were removed only after pin definitions compared
identical; remaining definitions were localized. Stock-library footprint
replacement was not used to suppress warnings. A metadata encoding error caught
during preparation was corrected, with accepted text/graphics restored before
final validation.

Historical sourcing conflicts were corrected without inventing replacement
identities. Candidate component ratings do not qualify the assembled system.

## Source and Manufacturing Validation

### Windows automated CAD evidence

KiCad CLI **9.0.7** produced the following retained results:

| Check | Common PCB | 200 W paired project | 2 kW paired project |
|---|---:|---:|---:|
| DRC errors / warnings | 0 / 48 | 0 / 48 | 0 / 48 |
| Unconnected PCB items | 0 | 0 | 0 |
| Schematic/PCB parity issues | 0 | 0 | 0 |
| ERC errors / warnings | — | 4 / 6 | 4 / 14 |

DRC warnings comprise 37 footprint-library comparisons, six missing courtyards
(J1/J2/J3/J5/T1/T2), two text-height findings, one diode-reference mask-clipping
finding and two diode-area silkscreen overlaps. The earlier refilled 200 W result
had 42 ordinary warnings; six formerly ignored courtyard checks were exposed.
The original 2 kW geometry had 39 warnings and lacked the larger diode lands;
its common-board copy adds the corresponding three silkscreen findings.

The four ERC errors per schematic are two undriven externally supplied
power-input findings and unused U21 Q1/Q2 outputs at pins 5/9. The cascaded
divider uses inverted outputs; unused complementary outputs were not rewired
to silence diagnostics. Symbol-comparison warnings are six/fourteen, compared
with original five/twenty-three. No new connectivity errors or off-grid mounting
symbols were introduced. Component-type checking is enabled at warning level
and reports no findings. No checks were suppressed.

### Fabrication-rule comparison

Native metadata records 0.070 mm copper per side, 1.440 mm dielectric and
0.010 mm mask per side, nominal total 1.6 mm, FR-4 TG150, blue/white and leaded
HASL. This bookkeeping is not a qualified impedance-controlled stackup.

A separate 8-mil (0.2032 mm) diagnostic found 14 existing gaps approximately
0.2010–0.2025 mm and no track-width violations. Accepted rules retain 0.2 mm
clearance. This is a process-constraint mismatch, not a new accepted-rule DRC
regression. The disposable rule-check project also had missing-library-table
warnings; normal project checks used the correct local tables.

### CAM and package evidence

Nine Gerbers were parsed by the supplied standard-library KiCad-subset checker.
Supported features include metric absolute 4.6 coordinates, apertures/macros,
dark/clear polarity, regions and linear/circular interpolation. Unsupported
drawing commands are rejected. This utility is not a general fabricator CAM
engine.

Detector copper/mask/paste flashes match retained pad geometry and polarity.
Neither mask layer has separate via-center opening flashes: tenting is retained.
Edge.Cuts contains three closed four-edge rectangles.

There are 244 plated hits, no non-plated hits and no slots. Internal openings
are routed, so empty NPTH output is intentional.

| Drill diameter (mm) | Plated hits |
|---|---:|
| 0.300 | 12 |
| 0.500 | 202 |
| 0.710 | 3 |
| 0.750 | 6 |
| 1.000 | 12 |
| 1.100 | 5 |
| 3.200 | 4 |

B.Paste retains two grounded T1/T2 pin-5 apertures of 6 × 6 mm. No automated
placement/assembly package was generated or qualified.

All nine Gerber primitive inventories matched same-setting diagnostic exports
of the accepted common board. The ZIP contains exactly 19 members, with matching
loose payload bytes and passing CRC/SHA-256 checks. The job uses 70 × 102 mm
centerline dimensions instead of automatic 70.05 × 102.05 mm stroked bounds.

### Comparison with January manufacture

All 244 historical plated hits match within 0.002 mm rounding tolerance.
Back copper/mask/paste/legend and Edge.Cuts primitive inventories match exactly.
Front mask/paste each replace four historical detector flashes with SOD-123
geometry. Front copper replaces four detector flashes and three zone polygons,
with 537 other primitives shared. Fill-engine/clearance differences mean
historical zone fills are not claimed byte-identical.

Front legend shares 2320 primitives, with 59 historical-only and 52 supplied-only
primitives, including four mask-subtraction pad flashes and line changes around
detectors/nearby labels. Silkscreen overlaps remain disclosed.

### Distribution and preservation

Packaging corrections retain exact CAM bytes and use the canonical source
policy sha256-utf8-lf-v1. The manifest hashes payload bytes; the checksum list
also covers the manifest and ZIP. See
[distribution integrity](docs/distribution-integrity.md).

Prior preparation verified preserved original artifacts and hardware directories
by SHA-256. RayPowerMeter source/Git state remained unchanged. Schematic/PCB
previews were inspected for title/page boundaries, annotation readability,
mounting and polarity. Original photographic bytes were retained.

Portable CAD/BOM and manufacturing checks passed in a selected-tree diagnostic
copy without private Windows source folders, archives or Excel files.
A focused text scan found no selected owner-specific paths or credential
signatures; it was not a comprehensive privacy or legal certification.

### Documentation revision verification — 2026-10-11

Focused checks of the uncommitted documentation revision passed: both KiCad
XML netlists retained all 54 references, 30 nets, values, footprints, pin types
and library definitions. Only descriptive sourcing properties changed.
BOM differences are limited to sourcing/population notes; measured CSVs,
PCB bytes, photograph bytes, legal texts and retained CAM bytes are unchanged.

Metadata-only repacking passed 19-member ZIP/CRC/manifest correspondence and
20 exact checksum entries. Isolated prospective LF/CRLF distributions passed
the package checker under Python 3.11.4 on Windows, with Git attribute filtering
verified without staging the authority. These are simulated distributions,
not native Linux runs or clones of a new commit. A corrupted-package diagnostic
confirmed repacking fails before payload mutation.

## Cross-Platform Verification

RF StateSide independently reported the following check of a fresh GitHub clone:

| Item | Owner-reported result |
|---|---|
| Operating environment | Linux workstation |
| Source commit | 73ce330 |
| KiCad | 9.0.8 |
| Python | 3.14.4 |
| Manufacturing integrity | PASS |
| Schematic and common PCB | Opened successfully |
| Custom footprints | Visually inspected |
| Working tree after inspection | Clean |

This is owner-reported independent testing, not a Codex-executed Linux run.
It does not claim a complete KiCad 9.0.8 ERC/DRC rerun or acceptance of a future
commit containing the documentation changes.

## Licensing and Asset Provenance

The official CERN-OHL-P-2.0 LICENSE is retained. NOTICE records original project
attribution and modifications; formatting changes preserve its approved wording.
KiCad-derived library portions retain their upstream license and exception.

RF StateSide's original custom symbol families include SWRBridge, MC74AC74DR2G
and VR_10K_25turn_TH with related aliases. Twenty-six standard-derived definitions
retain KiCad attribution. The mixed collection is not exclusively CERN licensed.

The transformer image is original RF StateSide photography with ChatGPT-assisted
cropping/background cleanup, not an AI-generated physical sample illustration.
Image bytes and metadata remain intact. See
[asset provenance](docs/asset-provenance.md).

## Remaining Engineering Limitations

The supplied SOD-123 package has not received physical fabrication/test
acceptance. Fabricator review of approximately 0.2 mm clearance with 2 oz copper
is required. Transformer lead mapping, viewing-face orientation, insulation and
mechanical details remain incomplete.

Forward measurement evidence contains 19 points through 250 W and 14 points
through 1500 W for the respective configurations. The 2 kW 2500 W endpoint is
estimated; its older 2000 W estimate was inactive. The 200 W reflected multiplier
is experimental, and the 2 kW reflected table is not independently measured.

Dated RayPowerMeter observations include 15-point runtime capacity and forward
table selection for both paths. They are software integration limitations, not
new calibration measurements. See
[calibration traceability](calibration/profile-traceability.md) and
[known limitations](docs/known-limitations.md).

## Assessment Boundaries

This record does not establish independent laboratory certification, commercial
production qualification, complete frequency/power/temperature validation,
guaranteed accuracy, physical fabrication of the supplied SOD-123 package or
new firmware acceptance. Legal explanatory documentation does not replace the
official license or guarantee immunity from liability.

The documentation revision preserves engineering evidence while separating
ordinary project guides from internal preparation records. It is not an
authorization to publish, order hardware or operate RF equipment.
