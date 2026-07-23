import json
import sys
from pathlib import Path

REPORT = Path("reports/trivy-report.json")

if not REPORT.exists():
    print("❌ Trivy report not found.")
    sys.exit(1)

with REPORT.open("r", encoding="utf-8") as f:
    report = json.load(f)

summary = {
    "CRITICAL": 0,
    "HIGH": 0,
    "MEDIUM": 0,
    "LOW": 0
}

for result in report.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):

        severity = vuln.get("Severity", "UNKNOWN")

        if severity in summary:
            summary[severity] += 1

print("\n========== SECURITY SUMMARY ==========\n")

for key, value in summary.items():
    print(f"{key:<10}: {value}")

print("\n======================================\n")

with open("reports/policy-summary.txt", "w") as f:
    f.write("Security Summary\n")
    f.write("=====================\n")

    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

if summary["CRITICAL"] > 0:
    print("❌ Build Failed - Critical Vulnerabilities Found")
    sys.exit(1)

print("✅ Policy Passed")