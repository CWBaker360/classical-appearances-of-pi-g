# Reproducibility

## Requirements

- Python 3.10 or newer
- A standard Python installation; the verification script uses only `math`
- `pdflatex` to rebuild the paper

## Run the numerical illustration

From the repository root:

```bash
python scripts/verify_gaussian_pi_g.py
```

The expected final line is:

```text
normalized area: 0.99999999999999689
```

The result is a binary64 floating-point illustration, not a rigorous enclosure. The omitted Gaussian tail outside [-6,6] is approximately 3.814274020654151e-17. The larger observed normalization discrepancy reflects floating-point accumulation. The console output archive excludes unrelated environment startup messages.

## Rebuild the paper

From the repository root:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/classical_appearances_of_pi_g.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory paper paper/classical_appearances_of_pi_g.tex
```

The source uses a fixed publication date and a deterministic appendix page
break so the public PDF remains a stable ten-page document.
