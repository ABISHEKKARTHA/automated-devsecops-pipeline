import json
import sys
from pathlib import Path

REPORT = Path("reports/trivy-report.json")
SUMMARY = Path("reports/policy-summary.txt")

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

critical_fixable = []

for result in report.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):

        severity = vuln.get("Severity", "UNKNOWN")

        if severity in summary:
            summary[severity] += 1

        if severity == "CRITICAL":

            fixed_version = vuln.get("FixedVersion")

            if fixed_version:
                critical_fixable.append({
                    "package": vuln.get("PkgName"),
                    "cve": vuln.get("VulnerabilityID"),
                    "installed": vuln.get("InstalledVersion"),
                    "fixed": fixed_version
                })

print("\n========== SECURITY SUMMARY ==========\n")

for key, value in summary.items():
    print(f"{key:<10}: {value}")

print("\nFixable Critical Vulnerabilities:", len(critical_fixable))

SUMMARY.parent.mkdir(exist_ok=True)

with SUMMARY.open("w", encoding="utf-8") as f:

    f.write("DEVSECOPS POLICY REPORT\n")
    f.write("=======================\n\n")

    for key, value in summary.items():
        f.write(f"{key:<10}: {value}\n")

    f.write("\n")

    if critical_fixable:

        f.write("Fixable Critical Vulnerabilities\n")
        f.write("--------------------------------\n")

        for vuln in critical_fixable:
            f.write(
                f"{vuln['cve']} | "
                f"{vuln['package']} | "
                f"{vuln['installed']} -> {vuln['fixed']}\n"
            )

if critical_fixable:

    print("\n❌ POLICY FAILED")
    print("Fixable critical vulnerabilities detected.")
    sys.exit(1)

print("\n✅ POLICY PASSED")