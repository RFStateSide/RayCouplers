# Design history

## Original hardware development

RF StateSide developed 200 W and 2 kW directional-coupler configurations for use
with RayPowerMeter and RayRailSwSense. Both were fabricated by PCBWay, manually
populated using SMT reflow and tested during development.

The circuits share a common board concept and electrical topology. Their
resistor populations and transformer construction differ. Divider values and
detector devices were investigated during calibration experiments.

Early 2 kW development used 1N4148 detectors. BAT42W was subsequently selected
after testing showed better low-power response. BAT42W is present on the
physically inspected 2 kW board. Older manufacturing BOMs also contain BAT15-03W
and stale resistor values; they are not the authority for the supplied population.

Physical inspection established 2 kW R23 = 2.7 kΩ and C1/C2 = 10 nF. These values
are retained in the supplied schematic and BOM. Contradictory historical
annotations are preserved as explicitly old/new records in
[annotation-history.json](annotation-history.json), not as assembly instructions.

The transformers use Fair-Rite 5943001401 #43 cores and 21 AWG high-temperature
enameled copper wire. The 200 W configuration has 16 turns on one core per
transformer; the 2 kW configuration has 24 turns on two taped cores per
transformer. [Winding photographs](transformer-construction.md#historical-experimental-evidence)
show development samples, not separately verified production configurations.

## Historical fabrication

The January 3, 2026 production artifacts contain SOD-323 detector pads and four
grounded mounting holes. Historical PCBWay records include a forty-board order
and 2 × 2 supplier panelization. These records are retained privately.

The later historical 200 W native board has SOD-123 detector lands and four
grounded mounting positions. The historical 2 kW native board omits the four
mounting footprints. Their shared routing contains 200 segments and 214 vias.

## Supplied common PCB

The supplied board follows the historical 200 W geometry: 70 mm × 102 mm, two
internal openings, SOD-123 detector pads and four grounded 3.2 mm holes. It is
not an identical copy of the January manufactured revision.

The source organization provides one PCB authority and two population
schematics. Existing mounting positions are represented as H1–H4 on GND.
Connector footprint naming, jumper BOM inclusion and descriptive component
metadata were reconciled. Local libraries preserve working geometry and pin
definitions; zones were refilled and saved.

These changes preserve routing, placements, electrical connectivity and
configuration values. Historical silkscreen dates remain provenance rather than
a new package identifier. [P3-prep-01](../manufacturing/README.md) identifies the
supplied manufacturing package, which has not been physically fabricated and
tested.

## Measurements and continued development

The [calibration reference](../calibration/profile-traceability.md) preserves
measured forward data separately from estimates and reflected experiments.
Recorded measurements do not establish guaranteed accuracy for a new assembly.

The [engineering audit](../PUBLIC_RELEASE_AUDIT.md) records source consolidation
and validation evidence. [Known limitations](known-limitations.md) identify
remaining fabrication, assembly and operating boundaries.
