# Sourcing status and metadata corrections

BOMs are engineering population lists, not guaranteed procurement kits. No supplier inventory or lifecycle guarantee was established. Existing supplier numbers are historical candidates unless explicitly cleared as inconsistent.

- D1/D2: proposed Panjit BAT42W_R1_00001. Panjit specifies SOD-123, pin 1 cathode/pin 2 anode and cathode band. The tested manufacturer remains unknown. Incorrect 1N4148 supplier references were removed. https://www.panjit.com.tw/upload/datasheet/BAT42W_SERIES.pdf
- C1/C2: retain 10 nF. Samsung CL21B103KDCNNNC is a compatible 0805, X7R, 10 nF, +/-10%, 200 V candidate supported by the manufacturer's listing. It is not established as the actual tested-board manufacturer. Incorrect 0.1 uF metadata was corrected. https://product.samsungsem.com/mlcc/CL21B103KDCNNN.do
- 2 kW R1/R2/R3/R4/R5/R6: retain 100 ohm. Incorrect 56/510 ohm MPNs were cleared; exact replacement MPN remains unresolved. The historical 1%, 1 W, 2512 specification is retained as a source-derived candidate requirement, not an independently tested rating.
- R8/R12 and R20 descriptions now agree with their actual values. Capacitor datasheet references were aligned to the named candidates rather than unrelated historical links.
- J4: schematic and PCB use the same retained five-position 2.54 mm land pattern. Conflicting TE/On Shore/Phoenix descriptions did not establish a verified purchasable mating part. Manufacturer, MPN, supplier number and datasheet are unresolved.
- JP1/JP2: the 3-pin 2.54 mm header is a soldered component; a removable shunt is separate. Historical STC02SYAN is a shunt sourcing lead, not a verified 3-pin header MPN. Header sourcing fields were cleared, headers included in BOMs, and two shunts listed explicitly.
- T1/T2: owner now confirms Fair-Rite 5943001401 #43 cores, 21 AWG high-temperature enameled copper wire and 16/24 turns. Individual cores are separate procurement rows, not assembly MPNs. Physical lead mapping and insulation details remain unresolved.
- RF connector candidates, trim pot, ICs, LED and remaining components retain supported historical fields. Blank sourcing fields, particularly several 2 kW RF connectors, are explicitly unresolved. Panel hardware, header selection and M3 mounting hardware need actual mechanical fit review.

Candidate datasheet ratings do not establish the assembled coupler's voltage, thermal, RF power, frequency or accuracy limits. Supplier codes are not invented for unresolved entries. Historical pricing is retained only in original files.

## Focused Phase 3 sourcing review

The retained pin/pad geometry was checked against the available original records. No historical identity was established for blank header/J4/2 kW RF-connector fields. Supplier numbers were not invented.

- JP1/JP2: [Samtec TSW-103-07-G-S](https://www.samtec.com/products/tsw-103-07-g-s) is a compatible nominal geometric candidate: single row, three positions, 2.54 mm pitch and 0.635 mm square posts (0.898 mm diagonal versus retained 1.0 mm drills). Confirm tolerances, post/shunt engagement and available lead variant before purchase. This is not the identified historical header; BOM MPN remains blank. A stale shunt datasheet on the 2 kW header was cleared. Manufacturer drawings are linked and not redistributed.
- J4: [Phoenix Contact MPT 0,5/ 5-2,54 / 1725685](https://www.phoenixcontact.com/en-nl/products/pcb-terminal-block-mpt-05-5-254-1725685) is a matching footprint-family candidate, five positions at 2.54 mm pitch. Nominal 0.5 × 0.9 mm pins have 1.030 mm diagonal against retained 1.1 mm drills; fabrication tolerance/body/enclosure fit still requires review. This resolves a useful candidate, not the original conflicting manufacturer identity. BOM remains explicitly unresolved.
- J1/J2: the historical Amphenol 83-1R [manufacturer drawing](https://www.amphenolrf.com/en-us/assets/file/4065788640/) describes a panel connector. The custom three-land PCB pattern is not its four-hole panel mounting drawing; lead/attachment construction must be checked. Do not promote this to a verified drop-in PCB connector.
- J3: Adam Tech's [manufacturer catalog](https://app.adam-tech.com/products/index/category%3A3121/page%3A2?return=%2F) lists RF1-106-D-00-50-HDW as 50-ohm BNC PCB mount. Retained custom pads do not establish a complete mechanical fit from that catalog alone. J5 and several 2 kW connector identities remain unknown.
- 2 kW R1–R6: approved 100 ohm, historical 1%, 1 W, 2512 requirement retained. [Stackpole RMCF/RMCP catalog](https://www.seielect.com/catalog/sei-rmcf_rmcp.pdf) is the retained manufacturer reference; access was restricted during this review, so no exact 100-ohm ordering MPN was promoted as verified. Existing wrong-value MPNs remain cleared.
- Mounting hardware: four grounded 3.2 mm positions are verified. M3 fastener/standoff length, material, insulating needs and custom RF mechanical attachments depend on the enclosure and remain unspecified.

Commercial obsolescence or unknown historical manufacturer identity alone does not prevent an AS-IS reference release. Exact purchase/fit decisions matter before assembly; uncertain identities are disclosed rather than filled with assumed parts.
