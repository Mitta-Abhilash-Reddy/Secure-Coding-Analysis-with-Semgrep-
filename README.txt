SEMGRP DEMO PACK (Secure Coding Analysis Tool)

1) Install Semgrep (any one):
   - pipx install semgrep
   - pip install semgrep
   - Docker: docker run --rm -v "$PWD:/src" semgrep/semgrep semgrep --help

2) Unzip this pack and cd into it:
   cd semgrep_demo_pack

3) Run with local rules (works offline):
   semgrep --config rules.yaml sample_app

4) Run with community rules (requires internet; stronger detection):
   semgrep --config p/python sample_app

5) Fix one issue (example):
   - In app.py, change:
       output = subprocess.check_output(f"ping -c 1 {host}", shell=True)
     to:
       output = subprocess.check_output(["ping", "-c", "1", host])
   - Re-run Semgrep and capture a second screenshot showing reduced findings.

What to screenshot for your report:
   A) Terminal output from Semgrep (before fixes).
   B) The code lines flagged (your IDE or cat -n sample_app/app.py).
   C) Terminal output after your fix (fewer issues).

Tip:
   If 'p/python' is slow, use '--error' to only show high-severity, or '--max-target-bytes 2MB' for quick demos.