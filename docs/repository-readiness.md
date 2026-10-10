# Repository readiness and file-selection policy

The curated tree is prepared for owner-approved initial placement into **RFStateSide/RayCouplers**, initially private. No Git initialization, remote, commit or GitHub operation occurred. Private preparation readiness does not establish public rights clearance or authorize publication.

Include README/LICENSE/NOTICE/.gitignore, hardware authorities and required project libraries/notices, both BOMs, reviewed engineering docs, attributed winding photograph, measured calibration CSVs, tools and one preliminary common manufacturing package. [Proposed inventory](repository-inventory.csv) records selection and review status; it is not an upload.

Exclude archive/, manufacturing/historical/, calibration/measurements/, generated/, validation/, Python/editor/KiCad local state, private external-model inventory and phase file lists. Excluded evidence remains unchanged. .gitignore is a guardrail, not access control: inspect selected files again before upload. Do not upload the entire local tree wholesale.

Before public publication, confirm custom CAD creators/download terms and required notices, approve photo provenance and final company/license/liability language, and approve file selection. The sources disclose unverified transformer physical lead mapping, sourcing/mechanical gaps, historical ERC/DRC exceptions, incomplete RF qualification and 0.2 mm versus 8 mil clearance. Such uncertainties can be disclosed in an AS-IS reference; manufacturing/operating claims require separate evidence.

Original workbook creator metadata requires owner selection. Initially track measured numeric excerpts with source-cell provenance. Owner may later approve originals or separately reviewed sanitized distribution copies; preserve originals either way.

Portable checks need no original development directories: `python tools/prepare.py --boms --projects`, `python tools/validate.py --portable`, `python tools/manufacturing.py --check`. Set KICAD_CLI to the installed executable. validation-baseline.json is an approved read-only geometry/netlist fingerprint, not another editable PCB. When private archives are absent, validation uses that fingerprint. Normal local validation additionally checks external preservation.

Next milestone: owner accepts Phase 3 package/docs/selection, then separately authorizes creation of the private organizational repository. Resolve final public rights/legal/engineering-status review before changing visibility. No next milestone is implemented here.
