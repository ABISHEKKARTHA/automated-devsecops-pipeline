import json
import sys
from pathlib import Path

TRIVY_REPORT = Path("reports/trivy-report.json")
ZAP_REPORT = Path("reports/zap-report.json")
SUMMARY = Path("reports/policy-summary.txt")

# -----------------------------
# Validate reports
# -----------------------------
if not TRIVY_REPORT.exists():
    print("❌ Trivy report not found.")
    sys.exit(1)

if not ZAP_REPORT.exists():
    print("❌ ZAP report not found.")
    sys.exit(1)

# -----------------------------
# Read Trivy Report
# -----------------------------
with TRIVY_REPORT.open("r", encoding="utf-8") as f:
    trivy = json.load(f)

summary = {
    "CRITICAL": 0,
    "HIGH": 0,
    "MEDIUM": 0,
    "LOW": 0
}

critical_fixable = []

for result in trivy.get("Results", []):

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

# -----------------------------
# Read ZAP Report
# -----------------------------
with ZAP_REPORT.open("r", encoding="utf-8") as f:
    zap = json.load(f)

zap_summary = {
    "HIGH": 0,
    "MEDIUM": 0,
    "LOW": 0,
    "INFO": 0
}

for site in zap.get("site", []):

    for alert in site.get("alerts", []):

        risk = alert.get("riskcode", "0")

        if risk == "3":
            zap_summary["HIGH"] += 1

        elif risk == "2":
            zap_summary["MEDIUM"] += 1

        elif risk == "1":
            zap_summary["LOW"] += 1

        else:
            zap_summary["INFO"] += 1

# -----------------------------
# Print Summary
# -----------------------------
print("\n========== DEVSECOPS SECURITY SUMMARY ==========\n")

print("TRIVY RESULTS")
print("----------------")

for key, value in summary.items():
    print(f"{key:<10}: {value}")

print("\nFixable Critical Vulnerabilities:", len(critical_fixable))

print("\nOWASP ZAP RESULTS")
print("----------------")

for key, value in zap_summary.items():
    print(f"{key:<10}: {value}")

# -----------------------------
# Write Report
# -----------------------------
SUMMARY.parent.mkdir(exist_ok=True)

with SUMMARY.open("w", encoding="utf-8") as f:

    f.write("DEVSECOPS POLICY REPORT\n")
    f.write("=======================\n\n")

    f.write("TRIVY RESULTS\n")
    f.write("-------------\n")

    for key, value in summary.items():
        f.write(f"{key:<10}: {value}\n")

    f.write("\n")

    f.write("OWASP ZAP RESULTS\n")
    f.write("-----------------\n")

    for key, value in zap_summary.items():
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

# -----------------------------
# Policy Decision
# -----------------------------
policy_failed = False

if critical_fixable:
    print("\n❌ POLICY FAILED")
    print("Reason: Fixable critical vulnerabilities detected.")
    policy_failed = True

if zap_summary["HIGH"] > 0:
    print("\n❌ POLICY FAILED")
    print("Reason: High-risk OWASP ZAP alerts detected.")
    policy_failed = True

if policy_failed:
    sys.exit(1)

print("\n✅ POLICY PASSED")