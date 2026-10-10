# Editing and regeneration

## Source authority

Edit PCB geometry only in `hardware/common/RayCouplers.kicad_pcb`. Edit the 200 W population in its paired schematic, and the 2 kW population in `hardware/variants/2kw/RayCouplers.kicad_sch`. Both projects use basename RayCouplers, matching existing symbol-instance project associations.

Keep reference designators, electrical pin mappings and shared connectivity synchronized across both schematics. Variant changes belong in instance fields and population documentation, not independent routing. Local symbol IDs preserve historical names; a name containing a resistor value is not a population selector. The instance Value and sourcing fields are authoritative.

Use the project-local symbol/footprint tables and standard KiCad 9 libraries. The existing working geometry differs from current stock libraries. Do not click automatic footprint replacement merely to remove comparison warnings. Custom footprints were exported with KiCad's native footprint API; no external STEP files were bundled.

After an authorized PCB edit, refill zones and save the common board in KiCad before regenerating. If updating from schematic, use the common project's 200 W schematic; inspect the diff and retain mounting pads, detector lands, RF geometry, and all approved placements. Never update the common board directly from a disposable 2 kW project.

## Derived outputs

```powershell
python tools/prepare.py --boms --projects
python tools/validate.py
```

`prepare.py` derives each disposable PCB from the common authority, changes population properties and schematic paths only, and writes under `generated/200w` and `generated/2kw`. These projects allow normal same-basename KiCad parity checks. They are ignored by Git and must never become design authorities.

BOM generation includes all 50 electrical/test-point references, jumper headers despite their former exclusion flags, and explicit mechanical/accessory rows. It groups only records whose value, package and sourcing/assembly information agree.

`validate.py` exports original and curated netlists, compares the original 50-reference electrical graph, checks approved geometry and population differences, validates both BOMs, runs ERC/DRC/parity, and verifies original-source hashes and preserved copies. It rejects new DRC errors, unconnected items, parity findings and unexpected ERC error categories.

Set `KICAD_CLI` to the executable path if needed. Python helpers use the standard library only. The local integrity check expects the original source paths recorded in `validation/source-baseline.json`. On another machine, run `python tools/validate.py --portable`: this validates CAD, geometry, BOMs and preserved copies without relying on the owner's original source folders. It cannot establish that those external folders remained unchanged.

The one-time construction script is preserved as inert text under `archive/phase2-construction/`, not a routine rebuilding command. It is not the current source authority.

The preliminary common manufacturing package is generated and checked with `python tools/manufacturing.py --export` and `python tools/manufacturing.py --check`; review [fabrication requirements](fabrication.md) first. Do not put disposable projects, logs, previews, or temporary comparisons into a release manufacturing package.
