# Editing and regeneration

## Setup and source authority

Install KiCad 9 with its stock libraries and Python 3, then work from the
repository root. Open hardware/common/RayCouplers.kicad_pro for the common PCB
and 200 W schematic. Open hardware/variants/2kw/RayCouplers.kicad_pro for the
2 kW population schematic. Project-local tables resolve relatively to
hardware/libraries/.

Edit PCB geometry only in hardware/common/RayCouplers.kicad_pcb. Keep reference
designators, electrical pin mappings and shared connectivity synchronized across
both population schematics. Both projects use basename RayCouplers, preserving
symbol-instance project associations. Variant populations do not require
independent routing.

A historical symbol name containing a resistor value is not a population
selector. Instance Value fields and the corresponding BOM are authoritative;
generic embedded-library defaults do not override the transformer recipe.

Use the local libraries and installed KiCad 9 stock libraries. Existing working
geometry differs from some current stock footprints. Do not automatically
replace it merely to remove comparison warnings. No external STEP binaries
are required.

After an intentional PCB edit, refill zones and save the common board before
regenerating. If updating from schematic, use the paired common 200 W schematic.
Inspect the diff and preserve intended mounting pads, detector lands, RF geometry
and placements. Never update the authority from a disposable 2 kW project.

## Derived projects and BOMs

Generate disposable paired projects for validation:

```sh
python tools/prepare.py --projects
python tools/validate.py --portable
```

The generator derives both PCBs from the common authority, changing population
properties and schematic paths. It writes under generated/200w and generated/2kw.
These ignored copies support same-basename KiCad parity checks and are not
editable design authorities.

After population or sourcing-note changes, regenerate BOMs:

```sh
python tools/prepare.py --boms
```

Each BOM covers all 50 electrical/test-point references, including jumper
headers, plus mechanical/accessory requirements. Grouping requires matching
value, package and sourcing/assembly information. Routine verification need not
rewrite tracked BOMs. See [BOM interpretation](../bom/README.md).

## Validation environment and scope

The Python helpers use the standard library. KiCad CLI is needed for source
checks. Set KICAD_CLI when its executable differs from the default Windows path.
On Linux:

```sh
export KICAD_CLI="$(command -v kicad-cli)"
```

Portable validation uses the included geometry/connectivity fingerprint and
checks CAD, populations, BOMs, ERC, DRC and parity. Preserved originals are
checked when available; private development directories are not required.
The full local mode additionally uses private source-baseline records and
cannot establish preservation of external originals on an unrelated machine.

The [engineering audit](../PUBLIC_RELEASE_AUDIT.md) records existing ERC/DRC
exceptions and separate Windows/Linux evidence. Changes must be assessed against
that scope rather than described as physically validated by CAD checks.

## Manufacturing outputs

Read [fabrication requirements](fabrication.md) and
[distribution integrity](distribution-integrity.md). Use --check to verify
existing files, --repack for NOTICE/fabrication-document updates, and --export
only to rebuild manufacturing output from an intentionally changed source.

Do not include disposable projects, logs or temporary comparisons in the
manufacturing package. Source editing, fabricator acceptance, assembly inspection
and RF calibration are distinct activities.
