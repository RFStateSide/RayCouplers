# Common PCB fabrication — P3-prep-01

Copyright RF StateSide LLC. SPDX-License-Identifier: CERN-OHL-P-2.0.
Retain NOTICE and LICENSE with this source package.

P3-prep-01 identifies the common manufacturing package prepared on 2026-10-10.
Both populations use the same fabrication layers. The source authority is
hardware/common/RayCouplers.kicad_pcb in the repository. This SOD-123 revision
has not been physically fabricated and tested.

## Board construction

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
| Internal routed openings | Two 20 × 30 mm rectangles; reproduce supplied outlines, with corners subject to tool radius |
| Mounting holes | Four plated grounded 3.2 mm holes, retained copper annuli |
| Smallest drill | 0.3 mm plated |
| Supplier panelization | Optional fabrication-house arrangement; no PCBWay panel tooling supplied |

## Clearance and fabricator acceptance

The historical PCBWay order specified nominal 8/8 mil track/spacing. The supplied
layout uses a 0.2 mm netclass clearance (7.874 mil). A strict 0.2032 mm / 8 mil
diagnostic found 14 existing gaps of approximately 0.2010–0.2025 mm. Track widths
passed that comparison.

**This package is not strictly 8-mil spacing compliant.** The fabricator must
accept the actual clearance geometry with 2 oz copper in CAM review before
manufacture. A process that cannot accept it requires a layout change and new
validation; the historical order does not qualify this later revision.

Native stackup metadata expresses 0.070 mm copper per side, 1.440 mm dielectric
and 0.010 mm mask per side, maintaining nominal 1.6 mm total thickness. This is
CAD bookkeeping, not a certified laminate/foil/plating process prescription or
an impedance-controlled stack. Legacy epsilon_r and loss_tangent values have
not been verified for a selected supplier laminate. Finished copper requirements
take priority over an assumption of 1 oz equivalence.

## Gerbers and drills

Nine Gerbers provide both copper, mask, paste and legend layers plus Edge.Cuts.
Use the PTH drill file for plated vias, components and mounting holes. The NPTH
file is intentionally empty: internal openings are routed from Edge.Cuts, not
drilled. The drill maps/report record 244 plated hits, no non-plated hits and no
slots.

B.Paste contains two 6 × 6 mm apertures at the T1/T2 grounded pin-5 structure
pads. These historical features do not represent a second back-side SMT
population. Top legend is mask-clipped; retained reference overlaps and small
text remain limitations. Do not add plotter tool/drill marks to copper.

The Gerber job records nominal Edge.Cuts centerline dimensions. KiCad's automatic
70.05 × 102.05 mm stroked bounds are not the nominal board size.

## Historical and supplied geometry

January 2026 manufacture used SOD-323 detectors. This package uses SOD-123 pads:
1.2 × 1.2 mm, 3.3 mm centers, pad 1 cathode (K), pad 2 anode (A).
Historical 2 × 2 supplier panels and forty-board order records are separate
private evidence, not acceptance of this revision.

This is **Public Engineering Reference — AS-IS**. No guaranteed RF performance,
fitness, certification or continuous-power rating is supplied. Fabricator CAM
acceptance, assembly inspection and system-specific calibration are distinct
from CAD and distribution checks.

## Distribution verification

Release payloads retain exact bytes under Git attributes. ZIP members must
match their loose files, and output checksums hash exact bytes. The manifest's
source_hash_policy is sha256-utf8-lf-v1: UTF-8 PCB bytes with CRLF normalized to
LF and bare CR rejected. This is distinct from hashing raw platform-specific
source bytes.

In the source repository, docs/distribution-integrity.md explains verification.
Run python tools/manufacturing.py --check from the repository root. Packaging
documentation changes do not establish physical fabrication or alter CAM
geometry.
