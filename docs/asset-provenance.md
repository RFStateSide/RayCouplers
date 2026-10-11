# Asset provenance

RF StateSide LLC developed the original RayCouplers hardware. The supplied
materials distinguish original contributions, modifications and upstream-derived
elements. The project license does not override third-party rights.

| Included material | Authorship and treatment |
|---|---|
| Hardware designs, BOMs and engineering documentation | RF StateSide LLC original work and curated modifications; CERN-OHL-P-2.0 and project NOTICE |
| Custom symbol families | RF StateSide original drawings include SWRBridge, MC74AC74DR2G and VR_10K_25turn_TH, including related aliases |
| Custom footprint collection | RF StateSide custom work and modifications; retained KiCad starting elements remain subject to upstream terms |
| Standard KiCad-derived symbols | KiCad library contributors; CC-BY-SA-4.0 with KiCad-libraries-exception |
| Transformer photograph | Original RF StateSide photography with AI-assisted cropping and background cleanup |
| Official legal texts | Original licensors' authorship and wording retained |
| Manufacturer component information | Identification and datasheet links; candidate parts do not establish historical installation or fit |

## CAD collection

The local collection preserves pin definitions and working footprint geometry.
Twenty-six of its 31 symbol definitions match standard KiCad graphics/pin
definitions. Five nonmatching definitions belong to the original transformer,
logic-device and trimmer families identified above. Connector customizations
coexist with standard KiCad-derived elements.

See [library attribution](../hardware/libraries/README.md) for the included
definitions and upstream notices. Original authorship of custom work does not
erase obligations for retained upstream starting material. Do not identify the
entire mixed collection as exclusively CERN-OHL-P-2.0.

Project-local library tables use relative paths. Installed stock 3D models are
external KiCad-library references; no external STEP binaries are bundled.

## Photograph

[raycoupler_toroid.png](images/raycoupler_toroid.png) is a photograph of physical
experimental winding samples made during RF StateSide development. ChatGPT was
used to crop the photograph and clean up its background. The underlying physical
samples are not AI-generated.

The distributed image and its metadata are retained unchanged. It is an edited
photograph, not an unedited camera original, and does not establish final turn
counts or lead polarity. See [image attribution](images/README.md).

## Component information and retained evidence

Manufacturer links supply component data; vendor PDFs, drawings and model
binaries are not included. Public component identities and package dimensions
do not establish ownership of a vendor's CAD material.

Original measurement workbooks and historical supplier records are retained
privately. The repository supplies measured CSV excerpts with source-cell
references and summarizes relevant manufacturing history. Those private records,
backup collections and historical interactive BOM software are not part of the
supplied file set.

ChatGPT and Codex assistance is acknowledged in the
[Development Tools section](../README.md#development-tools). The supplemental
[engineering audit](../PUBLIC_RELEASE_AUDIT.md) is explicitly attributed.
