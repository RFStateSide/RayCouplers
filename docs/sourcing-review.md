# Component sourcing reference

The BOMs are population references, not guaranteed procurement kits. Historical
manufacturer and supplier fields do not establish current stock, lifecycle,
mechanical fit or the identity of parts fitted to every tested board.

## Detectors and passive components

- **D1/D2:** BAT42W is the selected detector. Panjit BAT42W_R1_00001 is a
  SOD-123 candidate, with pad 1 cathode, pad 2 anode and a cathode band. The
  tested manufacturer is unknown. See the
  [Panjit datasheet](https://www.panjit.com.tw/upload/datasheet/BAT42W_SERIES.pdf).
- **C1/C2:** 10 nF. Samsung CL21B103KDCNNNC is an 0805, X7R, ±10%, 200 V
  candidate supported by the
  [manufacturer listing](https://product.samsungsem.com/mlcc/CL21B103KDCNNN.do).
  It is not identified as the historically installed part.
- **2 kW R1–R6:** 100 Ω. Exact replacement MPNs are unresolved. The historical
  1%, 1 W, 2512 specification remains a source-derived candidate requirement,
  not an independently verified operating rating.
  [Stackpole RMCF/RMCP data](https://www.seielect.com/catalog/sei-rmcf_rmcp.pdf)
  is the retained manufacturer reference; no exact ordering MPN is established.
- Other passive fields retain supported historical information. Correct
  instance values and package geometry take precedence over incompatible
  purchasing records. Blank fields remain unresolved rather than assumed.

## Headers, terminal block and RF connectors

| Position | Existing information | Fit/identity boundary |
|---|---|---|
| JP1/JP2 | Three-position 2.54 mm headers; separate removable shunts | Historical STC02SYAN identifies a shunt sourcing lead, not a verified header MPN |
| J4 | Five-position 2.54 mm footprint with 1.1 mm drills | Conflicting historical manufacturer descriptions do not identify the installed mating part |
| J1/J2 | Historical Amphenol 83-1R panel-connector information | Custom three-land PCB pattern does not match a four-hole panel-mount drawing |
| J3 | Adam Tech RF1-106-D-00-50-HDW catalog entry, 50 Ω BNC PCB mount | Retained custom pads alone do not establish full mechanical fit |
| J5 and several 2 kW RF connectors | Incomplete sourcing fields | Historical identities and attachment construction remain unspecified |

[Samtec TSW-103-07-G-S](https://www.samtec.com/products/tsw-103-07-g-s) is a nominal
geometric candidate for JP1/JP2: one row, three positions, 2.54 mm pitch and
0.635 mm square posts. Their 0.898 mm diagonal compares with retained 1.0 mm
drills. Verify tolerances, lead variant and shunt engagement before purchase.
It is not the identified historical header; BOM MPNs remain blank.

[Phoenix Contact MPT 0,5/ 5-2,54 / 1725685](https://www.phoenixcontact.com/en-nl/products/pcb-terminal-block-mpt-05-5-254-1725685)
is a matching footprint-family candidate for J4. Nominal 0.5 × 0.9 mm pins have
a 1.030 mm diagonal against the retained 1.1 mm drills. Manufacturing tolerances,
body and enclosure fit remain unverified; the original manufacturer identity is
not resolved by identifying this candidate.

The [Amphenol drawing](https://www.amphenolrf.com/en-us/assets/file/4065788640/)
describes panel mounting; do not treat that part as a verified drop-in PCB
connector. The
[Adam Tech catalog](https://app.adam-tech.com/products/index/category%3A3121/page%3A2?return=%2F)
supports J3 identification but not a complete fit assessment. Verify center
conductor, grounded attachment and enclosure construction.

## Transformers and mechanical materials

T1/T2 use Fair-Rite 5943001401 #43 cores and 21 AWG high-temperature enameled
copper wire. Each 200 W transformer has 16 turns on one core; each 2 kW transformer
has 24 turns on two taped cores. [Construction details](transformer-construction.md)
include unresolved lead mapping and insulation information.

Individual cores are procured once in the BOM material row: two per 200 W board,
four per 2 kW board. Transformer assembly rows are not additional core orders.
Wire length, enamel class and tape specification are not fully recorded.

Four grounded 3.2 mm mounting positions accept an appropriately selected M3
fastener arrangement. Length, material, standoff height and insulation depend on
the enclosure. Panel hardware and custom RF attachments require actual fit review.

## Reading the BOM

The trim pot, ICs, LED and remaining components retain supported historical
fields. Compatible candidates are not guarantees of installed identity or
availability. Datasheet component ratings do not establish assembled-system RF
power, thermal, frequency or accuracy limits.

Manufacturer drawings are linked rather than redistributed. See
[BOM interpretation](../bom/README.md), [assembly](assembly/common.md) and
[known limitations](known-limitations.md).
