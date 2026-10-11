# RayCouplers website publication handoff

Prepared 2026-10-11 for https://rfstateside.com/projects/raycoupler. Website implementation, deployment and announcements are separate owner-authorized tasks. No website changes are part of Phase 5A.

## Required technical reconciliation

| Existing description | Accepted source baseline / action |
|---|---|
| 12 turns / 16 turns | 200 W: 16 turns on one core per T1/T2; 2 kW: 24 turns on two taped cores per T1/T2 |
| 115 x 70 mm board | One common 70 x 102 mm PCB, two 20 x 30 mm internal routed openings, four grounded plated 3.2 mm mounting holes |
| Increased copper/spacing or separate high-power layout for 2 kW | Both populations use the same PCB, nominal 2 oz copper each side and 1.6 mm FR-4 TG150; population and transformer construction differ |
| Optional AD8307 footprint | Remove as a current-release feature; no such footprint is demonstrated by the curated design. Historical/external integration concepts must be labeled separately |
| Unqualified connector compatibility | Retained custom lands do not establish drop-in SO-239/N-type or other connector fit; review actual mechanical construction |
| Conflicting -55/-58 dB targets, band/power/protection assurances | Separate historical measurement evidence, design targets and unverified current-revision capabilities; do not promise universal accuracy, frequency range, continuous power or trip response |
| Assembled/tested or ready-for-inline-use descriptions | Owner physically fabricated/tested historical configurations; curated common SOD-123 P3-prep-01 has not been fabricated or physically qualified |

Common construction: Fair-Rite 5943001401 material #43; 21 AWG high-temperature enameled copper wire; BAT42W detectors. A complete board needs two cores for 200 W or four for 2 kW. Physical winding polarity/lead routing remains to be verified; do not infer it from the experimental photograph.

Use the corrected image description: original RF StateSide LLC photograph of physically constructed development samples, cropped and background-cleaned using AI-assisted editing. Samples may differ from final winding configurations.

## Publication coordination

Canonical repository: https://github.com/RFStateSide/RayCouplers (plural). Hardware license: CERN-OHL-P v2.0 / CERN-OHL-P-2.0. Designation: Public Engineering Reference — AS-IS. Add the repository link and revise the source-release status only when the owner authorizes publication. A singular website project name need not force a URL change.

Make known limits discoverable: 0.2 mm clearance needs fabricator CAM acceptance with 2 oz copper; the layout is not strict 8 mil spacing compliant. Source publication does not guarantee certification, accuracy, fitness, operating range or power handling. Independent fabrication, assembly and system-specific calibration remain necessary. RayPowerMeter's deferred calibration software corrections are a separate project milestone.

Preserve historical RF measurement material as historical evidence with available test context. Do not attribute it to the untested SOD-123 release. Current website marketing descriptions cannot substitute for the curated source, BOMs and limitations.
