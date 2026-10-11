# Manufacturing distribution integrity

Phase 5A, 2026-10-11. P3-prep-01 remains the accepted preliminary manufacturing geometry; packaging corrections do not establish physical fabrication/test acceptance.

## Exact output bytes and canonical source bytes

.gitattributes disables text conversion only under manufacturing/release/, plus binary ZIP/PNG files. Release Gerbers, drills, maps, job, fabrication notes, notices, manifest and checksums retain their exact chosen bytes across Git objects, Windows/Linux checkouts and source archives. Ordinary source/documentation text retains normal Git handling. The common PCB has explicit `text eol=lf`.

Manufacturing file hashes and SHA256SUMS.txt always hash exact bytes, with no output normalization or mismatch acceptance. Every ZIP member must equal its loose payload byte-for-byte; the manifest hashes all 18 payload files. SHA256SUMS.txt hashes those files, manifest and ZIP (20 entries), excluding itself.

The manifest source_hash_policy is `sha256-utf8-lf-v1`: validate the source file as UTF-8, replace every CRLF pair with LF, reject bare CR, then SHA-256 the resulting bytes. Preserve all other bytes, whitespace and the final-newline state. This canonical source digest works for modified projects without Git history and ignores only platform line-ending differences. It is not a Git object ID and is not an arbitrary working-tree-byte hash. For this unchanged source it equals the initial committed LF PCB SHA-256: f5968cbb65470cbbabefd31855e7ddf999ca55b2be7ae0e339facd8ca6b15fc2.

The former 06be1fd9861445000ff3bf5cc2ca6fb232145bd82769c2cc29c734a79d1db77a digest identifies the CRLF export-time source representation. The corrected manifest retains that explicitly labeled historical value. Future exports use the canonical policy; any substantive source change invalidates the package until consciously re-exported. Output hashes remain independent exact-byte verification.

Phase 5A preserves accepted geometry-bearing bytes from the original ZIP. The ZIP must be repacked because the manifest gains explicit canonical hash semantics and NOTICE/fabrication documentation gains current distribution information. Repacking does not re-export CAM or change any Gerber/drill/map/job/report bytes. The canonical source check and all strict manifest/ZIP/checksum comparisons remain enabled.

## Proposed snapshot versus final clean clone

Before a corrected commit exists, only a prospective distribution snapshot can be tested. An isolated temporary Git index/repository can apply attributes without staging or committing the authoritative checkout. Phase 5A verification checks prospective object bytes and simulated core.autocrlf=true/false checkouts. This does not claim a corrected GitHub commit, live Linux CAD run or owner acceptance.

When the owner separately authorizes staging/commit, stage .gitattributes and the intended corrections, and explicitly run `git add --renormalize -- manufacturing/release/P3-prep-01` before reviewing the staged diff. This forces already-tracked release files to be stored under the new -text policy; a stat-cached status listing alone can omit unchanged working files whose prospective Git representation changes. These commands were not run in the authoritative repository during Phase 5A. Expect line-ending-only blob changes for retained generated payloads, not geometry changes.

After separately authorized commit/push, verify the exact new SHA from a clean clone or GitHub source download. On Linux, with Python 3 and KiCad 9 libraries/CLI installed:

```sh
git clone https://github.com/RFStateSide/RayCouplers.git
cd RayCouplers
git rev-parse HEAD  # compare with the owner-approved correction commit
export KICAD_CLI="$(command -v kicad-cli)"
(cd manufacturing/release/P3-prep-01 && sha256sum -c SHA256SUMS.txt)
python3 tools/manufacturing.py --check
python3 tools/prepare.py --projects
python3 tools/validate.py --portable
```

Open hardware/common/RayCouplers.kicad_pro for the common PCB and 200 W schematic; open hardware/variants/2kw/RayCouplers.kicad_pro for the 2 kW population schematic. Inspect library resolution and compare results with the documented historical exceptions. Portable validation is expected to retain disclosed ERC findings; it does not qualify physical hardware. Helpers write ignored generated/validation outputs. Do not run --export merely to test existing artifacts.

A GitHub source archive has no .git directory; omit the Git commands, identify its downloaded commit separately, and run the same checksum/helper commands from its extracted root. Private original projects/workbooks are not required. Owner Linux acceptance remains separate and pending until reported.
