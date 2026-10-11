# Asset provenance and proposed file inclusion

RF StateSide LLC is the owner-confirmed publisher/copyright holder for its original engineering work. Root CERN-OHL-P-2.0 preparation does not confer third-party rights. See [licensing review](licensing.md).

| Material | Evidence / obligations | Proposed inclusion |
|---|---|---|
| Curated schematics/PCB, company docs and BOMs | Owner identifies original project as RF StateSide LLC work; modifications recorded in NOTICE | Initial private repository; public after final owner/legal review |
| Standard embedded KiCad assets | KiCad library contributors; CC-BY-SA-4.0 with library exception | Retain notices; design exception differs from collection redistribution |
| Custom local CAD collection | Owner-created footprints, connector customizations and T1/T2 SWRBridge; KiCad-derived portions retain notices; MC74AC74DR2G/trimmer families and aliases are additionally owner-confirmed original drawings | Tracked source; public review status separate from file selection; see collection notice |
| Installed stock 3D models | External KiCad variable references | References only; no model binaries bundled |
| Removed external STEP references | Private path inventory; vendor permissions unknown | No STEP binaries or private path inventory in proposed repository |
| Winding photograph | Owner took the original photograph of physical development samples; AI-assisted cropping/background cleanup only; distributed bytes unchanged | RF StateSide attribution and editing disclosure; experimental samples, not verified final configurations |
| Original RayCoupler.jpg images | Preserved originals; exact image rights not independently established | Private archive only |
| Interactive BOM HTML | Embedded software copyright/license blocks, including MIT code; stale populations | Private preserved archive; no republication in this phase |
| Vendor datasheets/drawings | Manufacturer links; Samtec drawings carry proprietary notices | Links only; no vendor PDF/model/drawing bundled |
| PCBWay order PDF/old ZIPs | Historical fabrication evidence, private order/customer/account context and older geometry | Private archive; public engineering specifications summarized separately |
| Original Excel files | Exact files preserved; creator/last-modifier contain personal name | Excluded initially; measured CSV excerpts retain cell provenance |
| Backup ZIPs | Sixteen originals inventoried, not copied; may contain private/vendor state | Original offline/private history, no automatic upload |
| Diagnostics/caches/session data | Temporary exports, source paths, local fingerprints | Ignored; never manufacturing release inputs |

The official [KiCad library license](https://www.kicad.org/libraries/license/) distinguishes design/generated use from library collection redistribution. [Collection notices](../hardware/libraries/README.md), unmodified upstream LICENSE-KiCad.md and exception text are prepared. Owner authorship is confirmed for custom footprints and the SWRBridge transformer symbol. The owner additionally confirms drawing both MC74AC74DR2G/trimmer families, including their related aliases; no identified unresolved symbol-source question remains. Standard KiCad-derived portions retain their separate terms. Do not label the entire mixed collection solely CERN-OHL-P.

Privacy inspection identified personal creator metadata in workbooks, absolute CAD/model paths in historical designs/private inventories, and supplier order details in retained records. Curated hardware uses relative library tables and installed-library variables. No external STEP binaries, vendor PDFs, order forms, credentials or machine session settings are distributed. Inventory entries can name excluded records. The owner explicitly approves retaining the historical PCBWay order identifier in inventory and supporting tools as manufacturing provenance; private supplier records themselves remain excluded. A filename alone does not establish rights.

Preserve all excluded evidence locally. Later select a separately reviewed archival bundle of meaningful older designs; do not automatically upload every backup/order record. Confirm source/notice obligations before publishing historical interactive BOMs, vendor-derived CAD or original images. No historical file was deleted, rewritten or sanitized in place.
