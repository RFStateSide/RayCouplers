# Focused Phase 2 validation

Validated with KiCad CLI 9.0.7. Reports and diagnostic renders are in the ignored validation/ directory. Disposable paired projects are in generated/. They are not release fabrication files.

| Check | 200 W | 2 kW |
|---|---:|---:|
| ERC errors | 4 | 4 |
| ERC warnings | 6 | 14 |
| DRC errors | 0 | 0 |
| DRC warnings | 48 | 48 |
| Unconnected PCB items | 0 | 0 |
| Schematic/PCB parity issues | 0 | 0 |

## Preserved design and resolved findings

All 200 track segments, 214 vias, three outline/opening rectangles, all 54 footprint placements, all pads and footprint line/arc geometry compare unchanged against the approved 200 W board. Zone definitions, clearance settings and keepouts are unchanged; fill was regenerated and saved, removing the stale D2 clearance finding.

Both curated electrical netlists match both originals after excluding the added H1-H4 mechanical references on the existing GND net: 30 named nets and 50 electrical/test-point references. J4 remains 1 +3.3V, 2 FWD, 3 REF, 4 INT, 5 GND.

D1/D2 retain SOD-123 1.2×1.2 mm rounded pads with 3.3 mm center spacing, pad 1 cathode and pad 2 anode. F.Cu/F.Mask/F.Paste pad geometry is retained. The closed vertical silkscreen edge at local X=-2.36 mm marks the cathode side. D2 cathode is on the left in board coordinates; D1 is rotated 180 degrees and its cathode is on the right. The Panjit candidate specifies the same numbered polarity. Refilling yields no diode clearance error.

All four grounded plated 3.2 mm holes remain at (72,91), (72,185), (128,91), (128,185) mm, with the historical copper pads. Unique H1-H4 references and schematic representation replace duplicate REF**/extra-footprint parity findings. J4 footprint naming and jumper BOM exclusion flags were aligned; footprint filters now accept the actual retained packages.

The 2 kW legacy symbol-cache aliases were removed only after pin definitions compared identical. Remaining Ray-library symbols were made local while retaining their definitions. No footprints were automatically updated from installed stock libraries.

## Remaining DRC warnings

Both populations use the same common geometry, so both have the same 48 warnings: 37 library footprint comparisons, six missing courtyards (J1/J2/J3/J5/T1/T2), two text-height warnings, one diode-reference mask-clipping warning and two diode-area silkscreen overlaps.

Against the Phase 1 refilled 200 W result, 42 ordinary warnings remain plus six formerly ignored courtyard checks now set to warning. The original 2 kW 39-warning geometry did not include the larger diode lands; its generated release-population copy intentionally uses the common SOD-123 geometry and its three additional silkscreen warnings. No newly introduced electrical/fabrication error was accepted. Component-type checking is also set to warning and produces no findings.

## Remaining ERC findings and intentional topology

Four errors per schematic are pre-existing: two undriven power-input findings for externally supplied rails, and U21 Q1/Q2 outputs at pins 5/9 left unused. The existing divider uses inverted outputs for its cascade/output; those unused complementary outputs were not connected or altered simply to silence ERC. Supply entry is through J4; a later reviewed power-source/PWR_FLAG and explicit no-connect annotation cleanup is reasonable without changing circuitry. This phase records the exceptions without suppressing checks.

ERC warnings are library-symbol comparison metadata (six for 200 W, fourteen for 2 kW). The original results had five and twenty-three warnings respectively. Local library preparation and retained stock-symbol metadata explain the changed counts; there are no new connectivity errors or off-grid mounting symbols.

## BOM and preservation checks

Each CSV covers the exact 50 electrical/test-point references: 48 soldered/assembled components and two PCB test points. Four mechanical board features, two shunts and four mounting-fastener positions are listed separately. All twelve approved variant value differences are checked. R23=2.7k and C1/C2=0.01uF are retained for 2 kW. Purchasing gaps remain explicit.

SHA-256 checks passed for every copied original artifact and for both unchanged hardware source folders. The current RayPowerMeter source/assets inventory, Git status and HEAD are unchanged; generated build/cache directories were excluded from the source fingerprint. No commits, pushes, software builds, flashing, GitHub actions or RF hardware operation occurred.

Portable validation also passed. It verifies the copied historical artifacts, CAD and BOMs without claiming access to the owner's external originals. Original source/session status and local diagnostic files are intentionally excluded from the future curated repository.

Rendered schematic previews were inspected for page boundaries and annotation readability; the common-board preview and native pad/marker definitions were inspected for mounting and detector polarity. No physical RF or manufacturing performance was tested in this phase.
