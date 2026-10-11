# Project CAD libraries

The supplied libraries preserve working footprint geometry and electrical pin
definitions from the RayCouplers designs. Original RF StateSide contributions
and standard KiCad-derived elements retain distinct attribution and licensing.

## Files and project use

[RayCouplers.kicad_sym](RayCouplers.kicad_sym) contains 31 symbol definitions.
[RayCouplers.pretty](RayCouplers.pretty/) contains seven footprints:

- D_SOD-123_handSoldering
- MountingHole_3.2mm_M3_ISO7380_Pad_TopBottom_Gnd
- RF_Pad_HF
- RF_Pad_HF_Sm
- SOIC127P600X175-14N
- SWRVoltageTransformer
- TRIM_3296W1103LF

The common and 2 kW projects reference these files through project-local
symbol/footprint tables and relative KIPRJMOD paths. Install KiCad 9 stock
libraries as well. Installed stock 3D models remain external dependencies;
no external STEP binaries are bundled.

Open the supplied projects with their local tables. Do not automatically replace
working footprints with current stock-library versions merely to remove
comparison warnings. See [editing instructions](../../docs/editing-workflow.md).

## Original RF StateSide contributions

RF StateSide created the custom footprints, connector customizations and original
symbol families. The five nonmatching symbol definitions are:

| Family | Definitions |
|---|---|
| Transformer | SWRBridge |
| Logic device | MC74AC74DR2G; MC74AC74DR2G_legacy2kw |
| Trimmer | VR_10K_25turn_TH; 3296W1103LF_legacy2kw |

Original contributions are covered by the project CERN-OHL-P-2.0 notice.
Some footprint starting elements derive from KiCad; original custom work does
not remove upstream obligations for those retained elements.

A historical library name is not a population selector. The actual instance
Value and population BOM identify the component to fit.

## Standard KiCad-derived portions

Twenty-six local symbol definitions match KiCad 9 graphics/pin definitions,
including capacitors, resistors, coaxial connectors, jumpers, screw terminals,
Schottky diodes, LEDs and MCP6561U/TLV3501AID comparators. Original instance
metadata and connector customizations coexist with these definitions.

Attribution: KiCad library contributors. These portions retain CC-BY-SA-4.0
with KiCad-libraries-exception. Preserve [LICENSE-KiCad.md](LICENSE-KiCad.md),
[the exception](KiCad-libraries-exception.txt) and the
[official licensing explanation](https://www.kicad.org/libraries/license/).

Collection redistribution remains subject to the applicable upstream terms.
The design/generated-output exception does not waive obligations for
redistribution of the library collection itself. The root CERN notice does not
override those rights.

See [asset provenance](../../docs/asset-provenance.md), [NOTICE](../../NOTICE) and
the [engineering audit](../../PUBLIC_RELEASE_AUDIT.md) for source attribution and
localization history.
