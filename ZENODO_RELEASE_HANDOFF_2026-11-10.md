# Zenodo release handoff — Classical Appearances of pi_g

**Prepared:** 2026-11-10  
**Status:** Release preparation only — NOT evidence of a published Zenodo record, DOI allocation, successful checksum validation, or independent mathematical peer review.

## Publication identity

- **Title:** Classical Appearances of pi_g: A Geometric Substitution Note
- **Creator:** Baker, Wayne (as in the current manuscript/repository metadata; confirm the preferred display name in Zenodo)
- **Resource:** Publication / Preprint (expository companion note)
- **Manuscript version:** preprint-v1 (original manuscript date: 2026-07-05)
- **Deposit date:** use actual Zenodo publication date when published; do not backdate the upload
- **Keywords:** pi_g; geometric pi; geometric substitution; N-series; Gaussian integral; polygonal approximation; classical analysis
- **Source repository:** https://github.com/CWBaker360/classical-appearances-of-pi-g
- **Related works:** reference the existing pi_g verification and N-series papers; use their verified DOIs when entering Zenodo metadata
- **Rights:** Copyright (c) 2026 Wayne Baker. All rights reserved, consistent with LICENSE_NOTICE.md. Do NOT select CC BY or another open-content license without a deliberate rights decision. Confirm Zenodo's accepted licensing option before proceeding.

## Proposed Zenodo description / abstract

This expository note records representative classical formulae in which the circle constant pi is rewritten through a geometric limiting constant pi_g. Once the previously established identity pi_g = pi is assumed, the exact substitutions preserve the original classical identities. The note distinguishes the completed limit from finite polygonal approximants and includes a reproducible binary64 illustration using N-series scale cancellation and Gaussian normalization. The numerical illustration is a consistency check, not a proof of the Gaussian integral or an independent proof of pi_g = pi; no new classical identities or computational speed advantage is claimed.

## Files to select for a first deposit

- `paper/classical_appearances_of_pi_g.pdf` — principal ten-page manuscript.
- `paper/classical_appearances_of_pi_g.tex` — matching source (verify compilation).
- `scripts/verify_gaussian_pi_g.py` — standalone numerical illustration.
- `output/gaussian_pi_g_output.txt` — archived example output.
- `REPRODUCIBILITY.md` — instructions and floating-point qualification.
- `LICENSE_NOTICE.md` — permissions notice.
- `SHA256SUMS.txt` — **only** after regeneration and validation for the exact deposited package, or include a separately named release-package checksum file.
- `docs/geometric_recasting_classical_pi_formulas.pdf` — optional companion handout, clearly not a second independent proof.

It is also acceptable to upload a clearly named versioned ZIP containing these files, plus a plain PDF separately, provided the ZIP manifest matches the ZIP contents and there is no ambiguous manuscript version.

## Release gates — check each before publishing

- [ ] Search both published Zenodo records and authenticated unpublished drafts for the **exact title** and related titles; do not open a duplicate record when a draft/version exists.
- [ ] Build the paper from `paper/classical_appearances_of_pi_g.tex` using the two `pdflatex` invocations in `REPRODUCIBILITY.md`; check ten-page PDF and compare against the designated upload file.
- [ ] Run `python scripts/verify_gaussian_pi_g.py`; compare numeric output to `output/gaussian_pi_g_output.txt`. Minor last-digit changes between binary64 environments require disclosure, not silent replacement.
- [ ] Compute and verify SHA-256 for every file in the **actual release bundle**. The existing repository-wide manifest must not be declared verified merely because it exists; it may precede subsequent GitHub edits.
- [ ] Check title, author display, version, preprint type, old manuscript date versus new upload date, and rights against the uploaded PDF.
- [ ] Save Zenodo as a **draft**, preview the files and metadata, and only then publish.
- [ ] After publication, record the issued DOI in `CITATION.cff` and `README.md`, separately from the manuscript's original date and version, and update any checksum manifests affected by those edits.

## Claim boundary

Since pi_g = pi, substituting the exact limiting constant is an identity, not a discovery of new classical formulae. Finite pi_g approximants are not identical to pi and carry numerical error. The Gaussian calculation uses Simpson's rule on [-6, 6] in binary64 and is **not** a certified enclosure or a demonstration of an accelerated integration algorithm.

**This file is a deposit handoff and does not itself constitute a Zenodo upload.**
