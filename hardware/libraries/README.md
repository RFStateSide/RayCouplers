# Project CAD collection and attribution

This collection was extracted from historical embedded project assets and localized during release preparation. Electrical pin definitions and footprint geometry are retained. Owner-created work and third-party-derived material have distinct provenance; the root CERN notice does not override upstream rights.

## Confirmed owner work

The owner confirms creating the custom footprints and custom symbols, including connector customizations and the T1/T2 SWRBridge symbol. Original RF StateSide contributions are covered by the project CERN-OHL-P-2.0 notice. Some hand-soldering footprint starting material came from installed KiCad libraries; applicable KiCad-derived portions retain the upstream terms below. Commercial package names/dimensions alone are not evidence of third-party copying.

All seven curated footprint definitions are included: D_SOD-123_handSoldering, MountingHole_3.2mm_M3_ISO7380_Pad_TopBottom_Gnd, RF_Pad_HF, RF_Pad_HF_Sm, SOIC127P600X175-14N, SWRVoltageTransformer and TRIM_3296W1103LF. Owner authorship does not erase upstream obligations for retained KiCad starting elements. No external STEP binaries are bundled; installed stock models remain external dependencies.

## Standard KiCad portions

Twenty-six of the 31 local symbol definitions match installed KiCad 9 graphics/pin definitions (capacitors, resistors, coaxial connectors, jumper, screw terminal, Schottky diode, LED and MCP6561U/TLV3501AID comparators). Owner instance metadata and connector customization coexist with these standard definitions. Attribution: KiCad library contributors; CC-BY-SA-4.0 with KiCad-libraries-exception. Preserve [LICENSE-KiCad.md](LICENSE-KiCad.md), [exception text](KiCad-libraries-exception.txt) and the [official licensing explanation](https://www.kicad.org/libraries/license/). Collection redistribution remains subject to attribution/share-alike obligations; the design/generated-output exception does not waive collection obligations. Historical modifications/localization are described in NOTICE and the Phase 2/3 reports.

## Focused symbol provenance review — 2026-10-11

| Definitions | Evidence | Treatment |
|---|---|---|
| SWRBridge (T1/T2) | Owner explicitly confirms creating the transformer symbol | RF StateSide-owned original symbol; CERN-OHL-P-2.0 |
| MC74AC74DR2G; MC74AC74DR2G_legacy2kw | Historical rectangle/pin definition, onsemi device metadata; original authorship clarified directly by owner in Phase 5A | Owner additionally confirms drawing this family and its related alias; RF StateSide original symbol contribution, CERN-OHL-P-2.0 |
| VR_10K_25turn_TH; 3296W1103LF_legacy2kw | Historical Bourns metadata, PARTREV 05/16 and Manufacturer Recommendation field; original authorship clarified directly by owner in Phase 5A | Owner additionally confirms drawing this family and its related alias; RF StateSide original symbol contribution, CERN-OHL-P-2.0 |

The owner recalls that some symbols may originate from public DigiKey component downloads. On 2026-10-11, complete recursive master-tree indexes of the official Digi-Key/digikey-kicad-library and Digi-Key/digikey-partner-kicad-library were reviewed; neither contains paths matching MC74AC74, 3296W or SWRBridge. This does not exclude older revisions, differently named symbols or separately hosted CAD-provider downloads. It is not an exact-source identification.

The [DigiKey curated library](https://github.com/Digi-Key/digikey-kicad-library) and [partner library](https://github.com/Digi-Key/digikey-partner-kicad-library) describe CC-BY-SA-4.0 with a design exception, but their terms are not assigned to the four owner-confirmed original definitions merely because the owner recalls other historical downloads. Vendor device names, pinouts and public download availability do not establish authorship or unrestricted redistribution.

The owner answered the focused Phase 5A question by selecting "I drew both symbol families myself" for MC74AC74DR2G and VR_10K_25turn_TH, including their related aliases. This is direct authorship evidence resolving the four previously unconfirmed definitions. Together with the T1/T2 confirmation, all five nonmatching definitions have owner-confirmed original authorship. Twenty-six standard KiCad-derived definitions retain their upstream attribution/terms. No specific unresolved symbol-source question remains on this evidence; final owner/legal publication approval is separate. No symbol, pin definition, footprint or circuit was replaced.
