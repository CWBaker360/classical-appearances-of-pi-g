#!/usr/bin/env python3
"""Pre-deposit audit. Read-only: does not regenerate manifests or change manuscript."""
from __future__ import annotations
import argparse
import hashlib
import math
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paper/classical_appearances_of_pi_g.tex"
PDF = ROOT / "paper/classical_appearances_of_pi_g.pdf"
MANIFEST = ROOT / "SHA256SUMS.txt"


def verify_manifest():
    failures = []
    rows = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if len(line) < 67 or line[64:66] != "  ":
            failures.append("Malformed manifest line: " + line[:100])
            continue
        digest, rel = line[:64], line[66:]
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            failures.append("Invalid SHA-256 digest for " + rel)
            continue
        target = ROOT / rel
        if not target.is_file():
            failures.append("Missing " + rel)
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        rows += 1
        if actual != digest:
            failures.append("SHA-256 mismatch: " + rel)
    if rows == 0:
        failures.append("No valid manifest entries checked")
    print(f"Manifest: {rows} files hashed; {len(failures)} issues")
    for item in failures:
        print("  FAIL:", item)
    return not failures


def next_chord(c):
    return c / math.sqrt(2.0 + 2.0 * math.sqrt(1.0 - .25*c*c))


def numerical_check():
    n, c = 6, 1.0
    for _ in range(12):
        c = next_chord(c)
        n *= 2
    values = []
    for _ in range(3):
        values.append((n, n*c/2))
        c = next_chord(c)
        n *= 2
    q = [v for _, v in values]
    first = [(4*q[i+1]-q[i])/3 for i in range(2)]
    pi_g = (16*first[1]-first[0])/15
    h = 12.0/10000
    s = 2*math.exp(-36)
    for i in range(1, 10000):
        x = -6+i*h
        s += (4.0 if i%2 else 2.0)*math.exp(-x*x)
    area = (s*h/3)/math.sqrt(pi_g)
    print(f"Binary64: pi_g={pi_g:.17f}, normalized_area={area:.17f}")
    # Tolerance allows platform-specific last-place floating-point variation.
    ok = abs(pi_g-math.pi) < 2e-13 and abs(area-1) < 2e-13
    print("Numerical sanity check:", "PASS" if ok else "FAIL")
    return ok


def build_check():
    if not TEX.is_file() or not PDF.is_file():
        print("PDF check: FAIL — expected TeX or PDF missing")
        return False
    if shutil.which("pdflatex") is None:
        print("PDF check: NOT RUN — pdflatex not installed")
        return False
    with tempfile.TemporaryDirectory(prefix="pi_g_build_") as tmp:
        for _ in range(2):
            p = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-output-directory", tmp, str(TEX)],
                cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, timeout=120,
            )
            if p.returncode:
                print("PDF check: FAIL — pdflatex error")
                print("\n".join(p.stdout.splitlines()[-25:]))
                return False
        produced = Path(tmp) / "classical_appearances_of_pi_g.pdf"
        if not produced.is_file():
            print("PDF check: FAIL — no PDF generated")
            return False
        # A successful rebuild is not byte-for-byte equivalence of the archived PDF.
        # PDF metadata, timestamps and TeX engines can vary.
        info = shutil.which("pdfinfo")
        if info:
            p = subprocess.run([info, str(produced)], capture_output=True, text=True)
            page_line = next((s for s in p.stdout.splitlines() if s.startswith("Pages:")), "")
            print("Rebuilt PDF:", page_line or "page count unavailable")
            if page_line and page_line.split(":")[-1].strip() != "10":
                print("PDF check: FAIL — expected 10 pages")
                return False
        print("PDF source build: PASS (not an archived-PDF identity check)")
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true", help="Also compile TeX twice")
    opts = parser.parse_args()
    checks = [("numerical", numerical_check()), ("manifest", verify_manifest())]
    if opts.build:
        checks.append(("PDF build", build_check()))
    else:
        print("PDF build: NOT RUN (pass --build to test)")
    failed = [name for name, ok in checks if not ok]
    print("OVERALL:", "PASS" if not failed else "NOT RELEASE READY: "+", ".join(failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
