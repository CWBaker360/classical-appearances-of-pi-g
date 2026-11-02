# Classical Appearances of pi_g

**Author:** Wayne Baker  
**Date:** July 5, 2026  
**Status:** Expository companion note / source and reproducibility archive

This repository contains the paper:

> **Classical Appearances of \(\pi_g\): A Geometric Substitution Note**

The paper records representative classical formulae in which the usual circle
constant \(\pi\) is rewritten using the geometric limiting constant \(\pi_g\),
under the established identification

\[
\pi_g=\pi.
\]

## Read the paper

- [`paper/classical_appearances_of_pi_g.pdf`](paper/classical_appearances_of_pi_g.pdf)
- [`paper/classical_appearances_of_pi_g.tex`](paper/classical_appearances_of_pi_g.tex)

## Central distinction

The completed limiting constant is exact:

\[
\pi_g=\pi.
\]

A finite computational value is only an approximant:

\[
\pi_g^{(N)}\approx\pi_g=\pi.
\]

Thus exact substitutions use \(\pi_g\), while numerical demonstrations use
\(\pi_g^{(N)}\) and must retain their finite-precision interpretation.

## Numerical illustration

The included Python script constructs a second-order polygonal/N-series
approximant from

```text
N = 24576, 49152, 98304
```

and uses it in a finite-window Gaussian normalization calculation.

Run from the repository root:

```bash
python scripts/verify_gaussian_pi_g.py
```

The canonical output is archived at:

```text
output/gaussian_pi_g_output.txt
```

## Companion handout

The related one-page summary

```text
docs/geometric_recasting_classical_pi_formulas.pdf
```

places classical geometric formulas beside their \(\pi_g\)-forms. It is a
companion reference sheet, not a separate proof and not the principal paper.

## Claim boundary

This note does not claim new classical identities. Once \(\pi_g=\pi\) has been
established, the displayed substitutions are equality by replacement of
identical constants. The Gaussian computation is an illustrative finite-
precision consistency test.

## Related repositories

- [`nseries-pi-acceleration`](https://github.com/CWBaker360/nseries-pi-acceleration)
- [`baker-geometric-pi-verification`](https://github.com/CWBaker360/baker-geometric-pi-verification)
- [`scaling-cancellation-principle`](https://github.com/CWBaker360/scaling-cancellation-principle)

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── REPRODUCIBILITY.md
├── LICENSE_NOTICE.md
├── CHANGELOG.md
├── SHA256SUMS.txt
├── .gitignore
├── paper/
│   ├── classical_appearances_of_pi_g.tex
│   ├── classical_appearances_of_pi_g.pdf
│   └── README.md
├── scripts/
│   ├── verify_gaussian_pi_g.py
│   └── README.md
├── output/
│   ├── gaussian_pi_g_output.txt
│   └── README.md
└── docs/
    ├── abstract.md
    ├── claim_boundary.md
    ├── geometric_recasting_classical_pi_formulas.pdf
    ├── repository_description.md
    └── github_upload_checklist.md
```

## Rights

Copyright © 2026 Wayne Baker. All rights reserved unless otherwise stated.
