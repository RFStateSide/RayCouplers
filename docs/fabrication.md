# Common PCB fabrication — P3-prep-01

Copyright RF StateSide LLC. SPDX-License-Identifier: CERN-OHL-P-2.0. Retain NOTICE and LICENSE with this source package.

P3-prep-01 is a controlled preliminary preparation identifier assigned on 2026-10-10. It is not a historical production version, physical fabrication acceptance or public release tag. Source authority: hardware/common/RayCouplers.kicad_pcb. Both population variants use these same fabrication layers.

| Requirement | Intended construction |
|---|---|
| Material | FR-4 TG150 |
| Copper layers | 2 |
| Nominal finished board thickness | 1.6 mm |
| Finished copper | 2 oz on both sides; approximately 70 micrometres nominal CAD representation |
| Solder mask / legend | Blue / white |
| Surface finish | Leaded HASL, retained historical requirement |
| Via process | Tented on both sides; do not open via mask by default |
| Individual outline | 70 × 102 mm at Edge.Cuts centerlines |
| Internal routed openings | Two 20 × 30 mm rectangles; reproduce the supplied outlines, including original corners subject to tool radius |
| Mounting holes | Four plated grounded 3.2 mm holes, retained copper annuli |
| Smallest drill | 0.3 mm plated |
| Supplier panelization | Optional fabrication-house arrangement; no PCBWay panel tooling supplied |

The historical PCBWay order specified nominal 8/8 mil track/spacing. The curated layout uses a 0.2 mm netclass clearance (7.874 mil). A strict 0.2032 mm / 8 mil diagnostic found 14 existing clearance violations, with reported gaps about 0.2010–0.2025 mm; the original source geometry is retained. Track widths pass that diagnostic. Therefore **this package must not be described as strictly 8 mil spacing compliant**. A fabricator must accept the existing 0.2 mm clearance geometry and 2 oz construction in CAM review before manufacture; otherwise a separately authorized localized layout review is needed. This is a documented historical-rule mismatch, not a new routing regression.

Native stackup metadata now expresses 0.070 mm copper each side, 1.440 mm nominal dielectric, 0.010 mm mask each side, blue/white colors and leaded HASL. The dielectric adjustment keeps the nominal 1.6 mm total; it is bookkeeping, not a certified laminate/foil/plating process prescription or an impedance-controlled stack. Existing epsilon_r/loss_tangent fields are legacy estimates and have not been verified for a chosen supplier laminate. Finished copper requirements take priority over an assumption of 1 oz equivalence.

Use the separate PTH drill file for plated vias/component/mounting holes. The NPTH file is intentionally empty because there are no non-plated drilled holes; internal openings are routed from Edge.Cuts and are not drill hits. Drill maps/report document actual counts. No slots are present in the drill inventory.

Nine Gerbers represent both copper, both mask, both paste, both legend and Edge.Cuts. B.Paste intentionally contains two 6 × 6 mm apertures at the T1/T2 pin-5 grounded structure pads. These are retained historical features, not a second set of back-side SMT components. Top legend is mask-clipped in export; retained reference overlaps and small text remain documented. Do not add tool/drill marks to copper from plotting presets. Gerber job size is corrected to Edge.Cuts centerline dimensions; KiCad's automatic stroke-bound size is 70.05 × 102.05 mm and is not the nominal board size.

January 2026 historical manufacture used SOD-323 detectors. These newly generated files use the accepted SOD-123 pads (1.2 × 1.2 mm, 3.3 mm centers, pad 1 K / pad 2 A). They have not been physically fabricated or tested. Historical 2×2 supplier panels and forty-board order evidence remain separate private records.

This is Public Engineering Reference — AS-IS. No guaranteed RF performance, suitability, certification or continuous-power rating is supplied. Factory CAM acceptance, assembly inspection and system-specific calibration remain separate from the software/CAD validation recorded here. No boards were ordered.

## Distribution byte handling

P3-prep-01 CAM geometry is unchanged by the 2026-10-11 Phase 5A packaging correction. Release payloads retain exact bytes under Git attributes; loose files and ZIP members must match, and output checksums hash exact bytes. The manifest source_hash_policy sha256-utf8-lf-v1 identifies UTF-8 PCB bytes with CRLF normalized to LF (bare CR rejected), not platform-specific raw working-tree bytes. See docs/distribution-integrity.md in the source repository for clean-checkout verification. Physical fabrication and CAM acceptance remain separate.
