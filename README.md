# RayCouplers

RayCouplers is RF StateSide LLC's directional-coupler project for forward and
reflected RF detection, power measurement, SWR monitoring and protection-system
experiments.

**Public Engineering Reference — AS-IS.** The editable designs, population BOMs,
manufacturing files and historical measurements support study, independent
construction, modification and continued development.

## Overview

The project was developed for RF measurement and protection applications using
RayPowerMeter and RayRailSwSense. It provides 200 W and 2 kW population
configurations on one common PCB. These names identify configurations; they do
not establish guaranteed continuous-power capability or measurement accuracy.

The original hardware was fabricated, manually populated with SMT reflow and
tested during RF StateSide development. The supplied common PCB incorporates
curated source and documentation. Its SOD-123 manufacturing revision has not
itself been physically fabricated and validated.

## Features and Design

The circuits provide forward/reflected detector signals, an interrupt-selection
circuit and a cascaded frequency divider documented as divide by four. J4 carries
+3.3 V, FWD, REF, INT and GND. Transformer construction and resistor populations
differ between configurations.

See [configuration details](docs/variant-configurations.md) for component values,
interface assignments and the historical jumper settings.

## Hardware Configurations

| Item | 200 W | 2 kW |
|---|---|---|
| D1/D2 | BAT42W | BAT42W |
| R7/R11 | 3.3 kΩ | 3.9 kΩ |
| R8/R12 | 1.6 kΩ | 1.2 kΩ |
| R23 | 2.7 kΩ | 2.7 kΩ |
| C1/C2 | 10 nF | 10 nF |
| Turns per T1/T2 | 16 | 24 |
| Fair-Rite #43 cores per transformer | One | Two taped together |

Both configurations use Fair-Rite 5943001401 cores and 21 AWG high-temperature
enameled copper wire. Use the matching [population BOM](bom/README.md); the PCB's
default component values describe the 200 W configuration.

## Common PCB Design

The two-layer board measures 70 mm × 102 mm. It includes two routed internal
openings, four grounded 3.2 mm mounting holes and SOD-123 detector lands.

Open [the common KiCad project](hardware/common/RayCouplers.kicad_pro) for the PCB
and 200 W schematic. Open [the 2 kW project](hardware/variants/2kw/RayCouplers.kicad_pro)
for its population schematic. There is one authoritative editable PCB, not a
separate routed board for each population.

KiCad 9 and its stock libraries are required. Project-local custom libraries are
included; see [library information](hardware/libraries/README.md). For source
changes and derived projects, follow [the editing workflow](docs/editing-workflow.md).

## Transformer Construction

The 200 W configuration uses one toroid for each transformer; the 2 kW
configuration uses two taped toroids for each transformer. The [construction
guide](docs/transformer-construction.md) records materials, winding method,
schematic connections and an experimental photograph.

Physical lead mapping, winding orientation and insulation details are incomplete
in the historical records. Verify them before reproducing an assembly.

## Manufacturing and Assembly

The [P3-prep-01 manufacturing package](manufacturing/README.md) supplies one
Gerber/drill set for both configurations. Read [fabrication requirements](docs/fabrication.md)
and [package verification](docs/distribution-integrity.md) before manufacture.
The retained approximately 0.2 mm clearance requires fabricator CAM acceptance;
it is not strict 8-mil spacing compliance.

Follow [common assembly](docs/assembly/common.md), then the
[200 W](docs/assembly/200w.md) or [2 kW](docs/assembly/2kw.md) instructions.
Historical January 2026 fabrication used SOD-323 detector pads and is distinct
from the supplied SOD-123 package.

## Calibration and Testing

Historical forward measurements contain 19 points through 250 W for the 200 W
configuration and 14 points through 1500 W for the 2 kW configuration. Each new
system requires its own calibration.

[Calibration traceability](calibration/profile-traceability.md) distinguishes
measured data from estimated endpoints and experimental reflected adjustments.
The [engineering audit](PUBLIC_RELEASE_AUDIT.md) records automated CAD checks,
manufacturing integrity and separately reported Linux inspection. These checks
do not establish physical RF performance of the supplied revision.

## Repository Contents

| Location | Contents |
|---|---|
| [hardware/](hardware/) | Common PCB, population schematics and local libraries |
| [bom/](bom/) | Population and procurement reference CSVs |
| [calibration/](calibration/) | Measured excerpts and calibration traceability |
| [manufacturing/](manufacturing/) | Controlled common-PCB fabrication package |
| [docs/](docs/) | Construction, history, sourcing, limitations and licensing |
| [tools/](tools/) | Python generation and verification utilities |
| [PUBLIC_RELEASE_AUDIT.md](PUBLIC_RELEASE_AUDIT.md) | Attributed technical validation record |

Original measurement workbooks and supplier archives are retained privately.
They are not required to open the supplied designs or check the package.

## Development Tools

KiCad was used for schematic capture and PCB design. Python utilities support
source verification and manufacturing-package integrity checks. Git and GitHub
provide version control and access to the engineering source.

ChatGPT by OpenAI and OpenAI Codex assisted with engineering review,
documentation, source organization, validation and preparation of the
open-hardware reference. RF StateSide LLC performed the original hardware
design, assembly and historical RF testing.

## Known Limitations

The supplied SOD-123 revision has not received physical fabrication acceptance.
Calibration, connector fit, transformer construction and operating suitability
require verification for each implementation. Frequency coverage, temperature
dependence and complete measurement conditions are not established by the
available records. No commercial certification or guaranteed performance is
claimed. Read [known limitations](docs/known-limitations.md).

## License

Copyright RF StateSide LLC. Original project contributions are provided under
**CERN-OHL-P v2.0**, SPDX **CERN-OHL-P-2.0**. The official [LICENSE](LICENSE) is
authoritative; retain [NOTICE](NOTICE) and applicable third-party notices.

See [licensing](docs/licensing.md) and [asset provenance](docs/asset-provenance.md)
for scope and separately licensed material.

## Credits and Acknowledgments

RF StateSide LLC developed the original hardware and contributed the custom CAD
work. KiCad library contributors supplied the upstream elements identified in the
library notices. Manufacturer documentation supports component identification;
candidate parts are distinguished from historically installed parts.

Canonical repository: [RFStateSide/RayCouplers](https://github.com/RFStateSide/RayCouplers).
