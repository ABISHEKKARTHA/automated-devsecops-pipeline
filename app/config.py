class Config:
    APP_NAME = "Automated DevSecOps CI/CD Pipeline"

    VERSION = "1.0.0"

    ENVIRONMENT = "Development"

    AUTHOR = "Abishek V Kartha"

    DESCRIPTION = (
        "Automated DevSecOps CI/CD Pipeline with "
        "Integrated Vulnerability Scanning and Policy-Based Remediation"
    )

    SECURITY = {
        "trivy": "Pending",
        "owasp_zap": "Pending",
        "policy_engine": "Pending"
    }