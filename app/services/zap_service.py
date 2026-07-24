import json
import os


class ZapService:

    REPORT_PATH = "reports/zap-report.json"

    @staticmethod
    def get_summary():

        summary = {
            "fail": 0,
            "warn": 0,
            "info": 0,
            "pass": 0,
            "total": 0,
            "status": "NOT AVAILABLE"
        }

        if not os.path.exists(ZapService.REPORT_PATH):
            return summary

        try:

            with open(ZapService.REPORT_PATH, "r") as f:
                report = json.load(f)

            for site in report.get("site", []):

                for alert in site.get("alerts", []):

                    risk = alert.get("riskcode", "0")

                    if risk == "3":
                        summary["fail"] += 1

                    elif risk == "2":
                        summary["warn"] += 1

                    elif risk == "1":
                        summary["info"] += 1

                    else:
                        summary["pass"] += 1

            summary["total"] = (
                summary["fail"]
                + summary["warn"]
                + summary["info"]
            )

            if summary["fail"] > 0:
                summary["status"] = "FAILED"

            elif summary["warn"] > 0:
                summary["status"] = "WARNING"

            else:
                summary["status"] = "PASSED"

            return summary

        except Exception:
            return summary