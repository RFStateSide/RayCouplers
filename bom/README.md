# Population and procurement records

Copyright RF StateSide LLC. CERN-OHL-P-2.0; see [NOTICE](../NOTICE) and [LICENSE](../LICENSE).

Each variant CSV is regenerated from its authoritative schematic using tools/prepare.py --boms. Categories Electrical, Transformer assembly and PCB feature together cover exactly 50 unique schematic references: 46 ordinary soldered components, two custom transformers and two PCB test points. H1–H4 are four existing plated board features. Accessories account for two shunts and four mounting positions.

T1/T2 rows count complete custom assemblies, not purchasable Fair-Rite transformers. MAT-CORES counts individual Fair-Rite 5943001401 toroids once: two for 200 W, four for 2 kW. Do not add embedded cores a second time. MAT-WIRE specifies 21 AWG high-temperature enameled copper wire; blank quantity means as needed, not zero. MAT-TAPE is as needed for 2 kW taped stacks; tape on 200 W is optional retention. No wire length/tape MPN is invented. Reference-prefix MAT/ASSY rows are procurement requirements, not KiCad component references.

Retained historical or compatible candidate manufacturer entries are labeled in Sourcing_status; they are not verified availability, originals or assembled-system RF ratings. Review [sourcing](../docs/sourcing-review.md) before purchasing. Values, package geometry and reference coverage take precedence over stale archived purchasing fields.
