import json
from pathlib import Path
from datetime import datetime

REPORT = Path("reports/trivy-report.json")


def get_security_summary():

    if not REPORT.exists():
        return {
            "status": "No scan available"
        }

    with REPORT.open("r", encoding="utf-8") as f:
        report = json.load(f)

    summary = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "total": 0,
        "image": "devsecops-pipeline:latest",
        "last_scan": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    for result in report.get("Results", []):

        for vuln in result.get("Vulnerabilities", []):

            severity = vuln.get("Severity")

            if severity == "CRITICAL":
                summary["critical"] += 1

            elif severity == "HIGH":
                summary["high"] += 1

            elif severity == "MEDIUM":
                summary["medium"] += 1

            elif severity == "LOW":
                summary["low"] += 1

    summary["total"] = (
        summary["critical"]
        + summary["high"]
        + summary["medium"]
        + summary["low"]
    )

    summary["policy"] = (
        "FAILED"
        if summary["critical"] > 0
        else "PASSED"
    )

    return summary