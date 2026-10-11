# RayCouplers

RF StateSide LLC's historical 200 W and 2 kW directional-coupler engineering project.

**Public Engineering Reference — AS-IS.** Historical engineering source for study, modification and independent verification.

Copyright RF StateSide LLC. See [NOTICE](NOTICE).

Both historical configurations were fabricated, manually populated using SMT reflow, and tested by the owner with RayPowerMeter and RayRailSwSense. The curated common SOD-123 preparation baseline has not been independently established as a fabricated/tested release revision. Historical calibration is evidence, not a guarantee of accuracy for another assembly.

## Start here

Use KiCad 9 (validation performed with 9.0.7).

- **PCB authority and 200 W population:** open `hardware/common/RayCouplers.kicad_pro`. Its `.kicad_pcb` is the only curated PCB design authority; its `.kicad_sch` supplies the 200 W BOM.
- **2 kW population authority:** open `hardware/variants/2kw/RayCouplers.kicad_pro`. Its schematic supplies the 2 kW BOM. There is intentionally no independent PCB in this source directory.
- `hardware/variants/200w/README.md` identifies the common project's 200 W role.
- `bom/200w/RayCoupler-200w-population.csv` and `bom/2kw/RayCoupler-2kw-population.csv` are derived reference population lists.
- `hardware/libraries/` contains extracted portable project symbols and footprint geometry. Stock KiCad libraries remain required. Preserve retained footprint geometry rather than updating it automatically.

The board is common: 70 × 102 mm, two internal openings, four grounded 3.2 mm mounting holes, and SOD-123 D1/D2 pads. Population values and transformer construction differ; see [variant configurations](docs/variant-configurations.md).

## Evidence and limitations

Unchanged original projects and historical BOMs are preserved locally in the excluded `archive/original-projects/` evidence area; they are not required to open or validate the distributed source. Original measurement workbooks are preserved locally in the excluded `calibration/measurements/` evidence area; measured excerpts are in `calibration/reference/`; [calibration provenance](calibration/profile-traceability.md) separates measurements, estimates, derived values and experimental adjustments.

`manufacturing/historical/` contains historical fabrication artifacts. January 2026 Gerbers use SOD-323 pads and must not be manufactured as if they represented this preparation baseline. The new preliminary common-board [P3-prep-01 manufacturing package](manufacturing/release/P3-prep-01/) contains Gerbers, plated/empty non-plated drill files, drill maps, fabrication notes and a checked ZIP. It has not been physically fabricated/tested. Read [fabrication requirements](docs/fabrication.md), including the historical nominal 8 mil versus actual 0.2 mm clearance distinction.

Read [editing workflow](docs/editing-workflow.md), [validation assessment](docs/validation.md), [transformer construction](docs/transformer-construction.md), [sourcing review](docs/sourcing-review.md), and [known limitations](docs/known-limitations.md).

## Regeneration

From this directory with Python 3:

```powershell
python tools/prepare.py --boms --projects
python tools/validate.py --portable
```

The helper regenerates disposable projects in `generated/` for both populations, deriving their PCB geometry from the common authority. Never edit generated copies. Validation requires KiCad CLI; set `KICAD_CLI` to its executable when not at the default Windows installation path. The portable check uses the included approved geometry/connectivity fingerprint. The owner can run `python tools/validate.py` to additionally check the original local source folders and Git state.

## Publication direction

Publisher: RF StateSide LLC. Prepared hardware license: **CERN-OHL-P v2.0 (CERN-OHL-P-2.0)**. The unmodified official [LICENSE](LICENSE), project [NOTICE](NOTICE) and [license review notes](docs/licensing.md) are supplied for final owner/legal review. Owner-created CAD authorship and standard KiCad-derived portions are documented; see [asset provenance](docs/asset-provenance.md).

Canonical repository: https://github.com/RFStateSide/RayCouplers (plural). The initial engineering-reference commit exists. Public visibility, release approval and website coordination are separate owner decisions; see [repository readiness](docs/repository-readiness.md).

## Assembly and release preparation

Use [common assembly](docs/assembly/common.md), [200 W assembly](docs/assembly/200w.md) or [2 kW assembly](docs/assembly/2kw.md). Both use Fair-Rite 5943001401 #43 cores and 21 AWG high-temperature enameled copper wire: 16 turns on one core per transformer for 200 W, 24 turns on two taped cores per transformer for 2 kW. The [owner photograph](docs/transformer-construction.md), cropped and background-cleaned with AI assistance, shows physical development samples rather than verified final winding configurations; physical polarity/lead mapping remains to be verified.

[Repository file-selection policy](docs/repository-readiness.md) distinguishes distributed files, excluded historical evidence and remaining symbol provenance review. [Distribution integrity](docs/distribution-integrity.md) explains byte handling and clean-checkout verification; [website handoff](docs/website-publication-handoff.md) records separately authorized website work. Review [Phase 3 validation](docs/phase3-validation.md) before accepting the preparation package. Related RayPowerMeter software supplies measurement/calibration integration; its deferred software corrections are independent and were not implemented here.
