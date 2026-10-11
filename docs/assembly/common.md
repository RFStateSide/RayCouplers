# Common-board assembly

Copyright RF StateSide LLC. CERN-OHL-P-2.0; see [NOTICE](../../NOTICE) and
[LICENSE](../../LICENSE).

Select the [200 W instructions](200w.md) or [2 kW instructions](2kw.md) and its BOM before
placing parts. The common P3-prep-01 fabrication package uses the supplied SOD-123
geometry. It has not been physically fabricated or RF-qualified in this curated
configuration. Historical January SOD-323 Gerbers are not interchangeable release
fabrication files.

## Preparation and population

1. Inspect the bare board against the common PCB: 70 × 102 mm, two routed internal
   openings, four grounded 3.2 mm holes and SOD-123 D1/D2 pads. Review [fabrication
   requirements](../fabrication.md), including the 0.2 mm versus nominal 8 mil clearance
   distinction.
2. Verify all parts against the selected 50-reference population list. T1/T2 are custom
   assemblies; TP1/TP2 and H1–H4 are PCB features, not purchased components. Include two
   three-pin headers and two removable shunts. Wire, cores, tape and enclosure mounting
   parts are separate requirements.
3. Check IC pin 1, LED polarity and capacitor type against the actual footprint and
   manufacturer drawing. Existing native artwork is the placement authority. Do not update
   footprints automatically to match current libraries.
4. The original boards were manually SMT-populated and oven-reflowed. Select a process
   suitable for the actual solder paste and components; no historical temperature/time
   profile is supplied. Do not assume through-hole connectors, custom wire assemblies or
   taped ferrites tolerate that reflow process.
5. Construct and install T1/T2 using [transformer
   documentation](../transformer-construction.md) only after resolving the physical
   lead/polarity mapping. Inspect enamel, stripped termination areas, winding clearances
   and retention before installation.

## Detector orientation

D1/D2 are BAT42W on SOD-123 pads. Pad 1 is cathode (K), pad 2 anode (A). The cathode band
on the selected diode must go to pad 1. In the native top view, D2 cathode is left; D1 is
rotated 180° and its cathode is right. Each pad is 1.2 × 1.2 mm with 3.3 mm center
spacing. The closed footprint silkscreen edge marks the cathode side; use pad/net
numbering if nearby reference lettering is clipped or overlaps. The Panjit candidate part
is a sourcing candidate, not an established tested-board manufacturer.

## Connectors and jumpers

J2 is RF IN; J1 is RF OUT. J3/J5 are coaxial sampling/interface connectors: use the
schematic nets and original mechanical construction rather than treating their retained
custom solder lands as a universal connector mounting pattern. Confirm center conductor to
pad 1 and outer conductor to grounded pad 2. Exact panel attachments/lead arrangement
require fit review. Each T1/T2 retains a back-side grounded pin-5 structure pad with a 6 ×
6 mm paste aperture; the physical shield/conductor construction still needs verification.

J4 pin assignments: 1 +3.3 V, 2 FWD, 3 REF, 4 INT, 5 GND. Match pin numbers, not assumed
cable colors or a connector viewed from the opposite face. Retained pitch is 2.54 mm, five
pins, 1.1 mm drill. Confirm the chosen terminal body and enclosure clearance.

Install one shunt on each JP1/JP2. Both at 1–2 select the historical SWR interrupt
arrangement (noted 3:1); both at 2–3 select power interrupt with VR1 threshold adjustment.
These settings retain the design notes and do not guarantee threshold accuracy. Identify
numbered pads before fitting shunts; do not infer polarity from the photograph. Mixed
positions are not the documented operating configuration.

## Mounting and first-power inspection

Use four M3 mounting positions through the grounded plated 3.2 mm holes. Choose
fasteners/standoffs for the actual enclosure and stack height; lengths/materials are
unspecified. Check unintended shorts to pads, bare wire and enclosure metal. Grounded
mounting pads do not independently establish a complete RF enclosure/bonding design.

Inspect correct variant values, diode/IC/LED orientation, solder joints, bridges,
connector pin mapping, transformer continuity and insulation, and shunt settings. Verify
the +3.3 V supply wiring and absence of unintended supply shorts before connecting the
related instrumentation. The native schematic has externally supplied rails and
intentionally unused U21 outputs; see [validation
exceptions](../../PUBLIC_RELEASE_AUDIT.md#source-and-manufacturing-validation). CAD and
file checks do not replace physical inspection or RF testing.

Establish calibration and verify interrupt behavior for the built system before relying on
measurements or protection. Historical curves are reference evidence only. The names 200 W
and 2 kW are population designations, not guaranteed continuous-power or accuracy ratings.
Use suitable operating precautions for the actual RF installation; application compliance
remains the builder's responsibility.
