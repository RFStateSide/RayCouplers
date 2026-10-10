# Asset provenance and proposed file inclusion

RF StateSide LLC is the owner-confirmed publisher/copyright holder for its original engineering work. Root CERN-OHL-P-2.0 preparation does not confer third-party rights. See [licensing review](licensing.md).

| Material | Evidence / obligations | Proposed inclusion |
|---|---|---|
| Curated schematics/PCB, company docs and BOMs | Owner identifies original project as RF StateSide LLC work; modifications recorded in NOTICE | Initial private repository; public after final owner/legal review |
| Standard embedded KiCad assets | KiCad library contributors; CC-BY-SA-4.0 with library exception | Retain notices; design exception differs from collection redistribution |
| Custom local CAD collection | Historical My/my/Ray definitions; some original creator/vendor origin uncertain | Private review; provenance confirmation before public redistribution |
| Installed stock 3D models | External KiCad variable references | References only; no model binaries bundled |
| Removed external STEP references | Private path inventory; vendor permissions unknown | No STEP binaries or private path inventory in proposed repository |
| New winding photograph | Owner-identified RF StateSide website image, unchanged filename/hash | Company attribution; final owner provenance review |
| Original RayCoupler.jpg images | Preserved originals; exact image rights not independently established | Private archive only |
| Interactive BOM HTML | Embedded software copyright/license blocks, including MIT code; stale populations | Private preserved archive; no republication in this phase |
| Vendor datasheets/drawings | Manufacturer links; Samtec drawings carry proprietary notices | Links only; no vendor PDF/model/drawing bundled |
| PCBWay order PDF/old ZIPs | Historical fabrication evidence, private order/customer/account context and older geometry | Private archive; public engineering specifications summarized separately |
| Original Excel files | Exact files preserved; creator/last-modifier contain personal name | Excluded initially; measured CSV excerpts retain cell provenance |
| Backup ZIPs | Sixteen originals inventoried, not copied; may contain private/vendor state | Original offline/private history, no automatic upload |
| Diagnostics/caches/session data | Temporary exports, source paths, local fingerprints | Ignored; never manufacturing release inputs |

The official [KiCad library license](https://www.kicad.org/libraries/license/) distinguishes design/generated use from library collection redistribution. [Collection notices](../hardware/libraries/README.md), unmodified upstream LICENSE-KiCad.md and exception text are prepared. Original authors/download terms for nonstandard content still require confirmation. Do not label the entire mixed collection solely CERN-OHL-P.

Privacy inspection identified personal creator metadata in workbooks, absolute CAD/model paths in historical designs/private inventories, and supplier order details in retained records. Curated hardware uses relative library tables and installed-library variables. No external STEP files, vendor PDFs, order forms, credentials or machine session settings are in the selected repository inventory. A filename alone does not establish rights.

Preserve all excluded evidence locally. Later select a separately reviewed archival bundle of meaningful older designs; do not automatically upload every backup/order record. Confirm source/notice obligations before publishing historical interactive BOMs, vendor-derived CAD or original images. No historical file was deleted, rewritten or sanitized in place.
