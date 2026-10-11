# Manufacturing distribution integrity

The P3-prep-01 package is tied to the common PCB by a canonical source
fingerprint. Its loose files, ZIP payload and checksum records must agree.
File integrity does not establish physical fabrication or RF performance.

## Exact output bytes

[.gitattributes](../.gitattributes) disables text conversion under
manufacturing/release/ and for binary ZIP/PNG files. Gerbers, drills, maps, job
metadata, package documentation, notices, manifest and checksums retain exact
bytes across Git objects and Windows/Linux checkouts. Ordinary source text uses
normal Git handling; the common PCB explicitly uses text eol=lf.

The manifest hashes 18 payload files. The ZIP contains those files plus the
manifest: 19 members. SHA256SUMS.txt hashes the 18 payload files, manifest and
ZIP, excluding itself: 20 entries.

Hashes use exact output bytes. Every ZIP member must equal its loose file
byte-for-byte. Line-ending normalization is not an acceptable output mismatch.

## Canonical source fingerprint

The manifest policy **sha256-utf8-lf-v1** performs these steps on the PCB source:

1. Validate UTF-8.
2. Replace CRLF pairs with LF.
3. Reject remaining bare CR.
4. SHA-256 the resulting bytes, preserving all other bytes and newline state.

This policy ignores only source line-ending differences. It is not a Git object
ID. For the supplied unchanged source the digest is:

```text
f5968cbb65470cbbabefd31855e7ddf999ca55b2be7ae0e339facd8ca6b15fc2
```

The manifest separately retains the historical raw export-time source digest
under source_export_bytes_sha256. A substantive source change invalidates the
existing package. Re-export and validate intentionally changed manufacturing
source rather than changing the expected source hash to silence a failure.

## Check an existing distribution

From the repository root with Python 3:

```sh
python tools/manufacturing.py --check
```

On Linux, the independent checksum check is:

```sh
(cd manufacturing/release/P3-prep-01 && sha256sum -c SHA256SUMS.txt)
```

The Python checker verifies canonical source identity, manifest payload hashes,
ZIP membership/CRC and exact loose-file correspondence, package inventory,
checksums and supported geometry features. It uses the standard library and
does not export CAM. It writes diagnostics under ignored validation/phase3/.

A source archive does not require Git history or private measurement workbooks.
For a checkout, identify the revision with git rev-parse HEAD. For an archive,
record the source revision supplied with the download.

## Update documentation without re-exporting CAM

After changing the root NOTICE or repository fabrication notes, run:

```sh
python tools/manufacturing.py --repack
python tools/manufacturing.py --check
```

Repacking first validates the existing package and source fingerprint, copies
only those two documents, updates actual payload hashes, retains the export
metadata, rebuilds the ZIP and checksum list, and checks the result. It does not
run KiCad or rewrite Gerbers, drills, maps, job metadata or the drill report.

Review documentation and hash changes together. Preserve the source fingerprint
policy and Git attributes. For intentionally changed PCB manufacturing source,
use the separate --export workflow and inspect all resulting outputs.

## CAD and cross-platform checks

For source validation with KiCad 9 CLI and libraries installed:

```sh
python tools/prepare.py --projects
python tools/validate.py --portable
```

On Linux, set KICAD_CLI to the installed executable when required:

```sh
export KICAD_CLI="$(command -v kicad-cli)"
```

These commands create ignored generated/validation outputs. Portable validation
retains disclosed historical ERC findings; it does not qualify physical hardware.
Do not run --export simply to check existing artifacts.

See [editing instructions](editing-workflow.md), [fabrication](fabrication.md)
and the [engineering audit](../PUBLIC_RELEASE_AUDIT.md). The audit separately
records Windows automated checks and RF StateSide's reported Linux inspection.
