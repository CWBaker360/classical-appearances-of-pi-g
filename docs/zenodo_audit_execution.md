# Zenodo local audit execution — 2026-11-10

This is a **release gate**, not a declaration that the repository has passed it.

## On Windows (Git Bash or PowerShell)

From the repository root, after `git pull`:

```sh
python scripts/audit_zenodo_release.py --build
```

Requires Python 3, `pdflatex` on PATH, and optionally `pdfinfo` for the ten-page check. The script does **not** rewrite any files. It:

1. Runs an independent Python binary64 calculation using the same polygonal doubling, second-order Richardson, and Simpson steps.
2. Computes SHA-256 for all paths listed in `SHA256SUMS.txt` and fails on mismatches or missing entries.
3. Compiles the TeX twice in a temporary location; reports its page count if `pdfinfo` is installed.

A compiled PDF is not *automatically* proof that the archived PDF is byte-for-byte identical, nor is a binary64 check a rigorous error enclosure. The manuscript's numerical claims and the release payload must still be reviewed.

## When the manifest fails

The old manifest predates several repository changes; a failed checksum gate is expected until an **intentional new manifest** has been generated for the selected release commit. Do not edit numerical outputs or manuscript bytes to force a match. Preserve the old manifest under a clearly dated historical name, generate fresh hashes for the exact release file set, and rerun the checker. Do not commit a newly generated manifest until it has been checked.

For Zenodo upload, make a **separate manifest for the deposit bundle**, listing exactly the archive contents. Do not include the ZIP itself inside its own manifest.

## Zenodo

Before publishing, search the authenticated Zenodo dashboard for an existing upload draft, choose the intended rights, review metadata, preview the deposit, and only then publish. No DOI can be filled in until one is assigned. 
