# Secure Coding Analysis with Semgrep — Two-Page Report

**Student Name:** ____________________  
**Course/Section:** ____________________  
**Date:** 31-08-2025  
**Faculty:** ____________________  

## Abstract (≈150–200 words)

This report demonstrates a minimal **Secure Coding Analysis Tool** prototype using **Semgrep** (SAST) to meet the **CT-CS‑01 Secure Coding Analysis Tool** problem statement (Cyberthon 2025). We scan a small Python Flask codebase that intentionally includes insecure patterns (e.g., unsafe YAML loading, use of `eval`, and server-side template injection via `render_template_string`). The scan is executed locally using community rulesets (`p/python`, `p/secrets`). Findings are reviewed and mapped to secure coding practices and OWASP Top 10 categories. Remediation suggestions and re-scan verification are provided to show a measurable reduction of security risk in the code. The outcome is a lightweight, developer-friendly workflow that can be integrated into CI, addressing the objectives of automated code review, standards alignment, and risk minimization.

## Problem Statement (cite the source)
**ID:** CT-CS‑01 — Secure Coding Analysis Tool  
**Why this?** It asks for a tool that detects common code vulnerabilities, promotes secure coding practices, and scales via integration (CI/CD). Semgrep matches these needs.

## Method
1. Install Semgrep (pipx or Docker).  
2. Scan test app: `semgrep --config p/python --config p/secrets --json -o results.json --metrics=off`  
3. Review CLI findings and the JSON report.  
4. Fix issues, then re-scan to verify the risk reduction.

## Results (Screenshots)
Paste 2–4 screenshots (crop tightly):
- Terminal showing Semgrep summary (findings count).
- Selected findings detail in terminal.
- `results.json` opened in a viewer.
- (Optional) After-fix re-scan showing fewer/no findings.

## Sample Findings & Remediations
- **Unsafe YAML load** → use `yaml.safe_load` or `yaml.load(..., Loader=yaml.SafeLoader)`  
- **Use of `eval`** → replace with safe parsers / whitelisted operations  
- **`render_template_string`** → avoid dynamic templates; pass variables to static templates

## Conclusion (≈80–120 words)
Briefly state how the tool addresses CT-CS‑01: automated detection, actionable feedback, and integration potential. Mention future work: rule customization, multi-language scans, CI gate thresholds.

## References
- Semgrep Docs (install, run, rulesets)
- Problem statement PDF(s)
