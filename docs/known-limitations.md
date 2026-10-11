# Known limitations

RayCouplers is a **Public Engineering Reference — AS-IS**. Historical physical
testing does not establish certification, universal accuracy, guaranteed power
handling or suitability of later revisions and substitutions.

## Physical validation and operating evidence

The original hardware configurations were fabricated, assembled and tested.
The supplied SOD-123 common PCB and P3-prep-01 package have not themselves been
physically fabricated and validated. Automated CAD checks and successful file
inspection do not establish RF performance.

The records do not fully establish frequency coverage, instrument traceability,
temperature dependence, exact tested diode manufacturer or maximum-power
capability of the supplied revision. The names 200 W and 2 kW identify
configurations rather than independently qualified operating ratings.

## Manufacturing

The layout retains a 0.2 mm netclass clearance. A strict 8-mil (0.2032 mm)
comparison found 14 gaps of approximately 0.2010–0.2025 mm. The package must not
be described as strict 8-mil spacing compliant.

Fabricator CAM acceptance of the actual geometry with the specified 2 oz copper
is necessary before ordering. Historical PCBWay production does not establish
acceptance of every later refinement. See [fabrication requirements](fabrication.md).

Retained silkscreen overlaps, small labels, absent custom courtyards and library
comparison warnings are recorded in the [engineering audit](../PUBLIC_RELEASE_AUDIT.md).
Working geometry has not been modernized merely to clear those warnings.

## Transformer construction and component fit

Core identity, turn counts and wire gauge are established. Physical winding
start/polarity, viewing-face reference, coupled-conductor construction, grounded
structure and lead-to-pad mapping remain incomplete. Wire insulation class,
tape specification, retention and mechanical installation details are not fully
recorded. Do not energize an assembly based on an assumed mapping.

Use [transformer construction](transformer-construction.md) and verify physical
connections against an original device or a complete construction drawing.
Component sourcing candidates do not establish historical identity, availability,
connector mating or mechanical fit. See [sourcing information](sourcing-review.md).

## Calibration and software integration

Historical forward measurement evidence consists of 19 points through 250 W for
the 200 W configuration and 14 points through 1500 W for the 2 kW configuration.
Higher estimated firmware values are not additional measurements.

Each built system requires appropriate calibration and verification of its
interrupt behavior. See [calibration traceability](../calibration/profile-traceability.md)
for source cells, estimates and dated RayPowerMeter integration findings.
Software capacity and forward/reflected table handling can limit the use of the
historical data; no firmware correction or acceptance is supplied here.

## Electrical checks and safe operation

The schematics retain externally supplied power rails and unused U21
complementary outputs, producing disclosed ERC findings. They have not been
rewired merely to suppress diagnostics. Check supply wiring, component
orientation, insulation and unintended shorts before operation.

Use appropriate precautions for the actual RF installation and verify applicable
safety and regulatory requirements. No commercial certification, guaranteed
accuracy, fitness or protection threshold is claimed. The official
[LICENSE](../LICENSE) and approved [NOTICE](../NOTICE) govern the stated legal terms.
