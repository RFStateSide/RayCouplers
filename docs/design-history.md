# Preserved design history

The owner's two historical coupler configurations were fabricated by PCBWay, populated manually with SMT reflow, and tested with RayPowerMeter and RayRailSwSense. The originals remain in their development folders and unchanged copies are retained in archive/original-projects/.

Phase 1 established shared native routing (200 segments), 214 vias, 50 common footprint placements, 70 × 102 mm outline, and two internal openings. The current 200 W PCB was selected for consolidation because it already has SOD-123 detector lands and four grounded mounting holes.

January 3, 2026 production artifacts retain those four holes with SOD-323 detector pads. The current historical 2 kW native PCB omits the four mounting footprints. The common preparation PCB preserves the 200 W routing and larger diode pads; it is not an identical January fabrication revision.

The owner confirms BAT42W on the physically inspected 2 kW board. 1N4148 belonged to earlier development. Existing manufacturing BOMs also contain BAT15-03W and stale resistor values; those entries are not accepted as the tested population authority.

Owner inspection confirmed 2 kW R23=2.7 kohm and C1/C2=10 nF. Curated annotations now agree. Original contradictory annotations are preserved in docs/annotation-history.json and in unchanged archived schematics. Experimental reflected-calibration adjustments are historical and unsupported as universal corrections.

Phase 2 renamed board-only mounting references to H1-H4, represented them on the existing GND net in both schematics, aligned J4's footprint identifier, included jumper headers in BOMs, made custom assets portable and refilled zones. Geometry comparisons establish preserved track/via/outline/pad geometry. Mechanical symbol placement and metadata changes do not alter the electrical circuit.

The curated common baseline has not itself been independently demonstrated as physically fabricated/tested. Historical board silkscreen markings and dates are retained as provenance, not a new release identifier.

Phase 3 owner information establishes Fair-Rite 5943001401 #43 cores and 21 AWG high-temperature enameled wire, 16 turns on single cores for 200 W and 24 on taped double cores for 2 kW. Early 2 kW 1N4148 detector experiments preceded BAT42W adoption after owner testing for improved low-power response. The photograph records experimental variations, not verified separate production revisions. New P3-prep-01 manufacturing outputs are preparation files, not another historical fabricated revision.
