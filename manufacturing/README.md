# Common PCB manufacturing files

The [P3-prep-01 package](release/P3-prep-01/) contains one common fabrication
design for the 200 W and 2 kW populations. Its source is
[hardware/common/RayCouplers.kicad_pcb](../hardware/common/RayCouplers.kicad_pcb).

P3-prep-01 is a controlled package identifier. It does not establish physical
fabrication or RF testing of this SOD-123 revision.

## Package contents

The directory supplies nine Gerber layers, separate PTH/NPTH drill files,
SVG drill maps, a drill report, Gerber job metadata, fabrication notes, LICENSE,
NOTICE, a manifest, checksums and the manufacturing ZIP. The NPTH file/map is
intentionally empty: the two internal openings are routed from Edge.Cuts.

Use the appropriate [population BOM](../bom/README.md) and
[assembly instructions](../docs/assembly/common.md). The package contains no
population-specific duplicate Gerbers or automated placement/assembly package.

## Fabrication requirements

Read [fabrication notes](../docs/fabrication.md) before ordering. The 70 × 102 mm
board specifies nominal 1.6 mm thickness and 2 oz copper on both sides.
The retained approximately 0.2 mm clearance is not strict 8-mil compliance;
fabricator CAM acceptance is necessary.

Historical January fabrication used SOD-323 detector pads. This package uses
SOD-123 pads and is distinct from those physically manufactured boards.
Historical supplier records and panel tooling remain private.

## Verification and maintenance

From the repository root, check existing outputs without re-exporting them:

```sh
python tools/manufacturing.py --check
```

See [distribution integrity](../docs/distribution-integrity.md) for exact-byte
checks, source fingerprints and Windows/Linux behavior. Validation evidence and
exceptions are summarized in the [engineering audit](../PUBLIC_RELEASE_AUDIT.md).

After documentation-only changes, use the metadata-only repacking command
described in that guide. Export CAM with `python tools/manufacturing.py --export`
only when rebuilding manufacturing outputs from an intentionally changed source.
Exports may differ across timestamps and KiCad versions; inspect the resulting
geometry and distribution rather than assuming byte-stable regeneration.
