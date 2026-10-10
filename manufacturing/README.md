# Historical evidence and common release preparation

Everything under historical/ remains preserved unchanged and is excluded from the proposed initial repository because it contains private supplier records and earlier geometry. January Gerbers use SOD-323 detectors; the accepted common release preparation uses SOD-123. Original supplier panels are not required by the individual-board design.

The [P3-prep-01 package](release/P3-prep-01/) contains one common fabrication design for both populations. See [fabrication notes](../docs/fabrication.md) and the [validation assessment](../docs/phase3-validation.md). Generated output is tied to the common authority by SHA-256 in its manifest. The package includes the official license and project notice, but no vendor datasheets, private orders, population-specific duplicate Gerber sets or disposable CAD projects.

Run `python tools/manufacturing.py --export` to regenerate the controlled preliminary package directly from hardware/common/RayCouplers.kicad_pcb; run `python tools/manufacturing.py --check` to validate existing outputs. Outputs are not byte-stable across timestamps/KiCad releases; geometry and manifest hashes are checked instead.

Physical fabrication/test acceptance has not been performed. The preserved layout requires 0.2 mm clearances rather than strict historical nominal 8 mil; a fabricator must accept that distinction with 2 oz copper. No manufacturing order, GitHub release or publication occurred.
