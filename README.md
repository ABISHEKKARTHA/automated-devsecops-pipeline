# Automated DevSecOps CI/CD Pipeline with Integrated Vulnerability Scanning and Policy-Based Remediation

## Overview

This project demonstrates an automated DevSecOps CI/CD pipeline that integrates security into every stage of the software development lifecycle. The pipeline automatically builds, tests, scans, and validates a containerized Flask application using GitHub Actions.

The solution combines Static and Dynamic Application Security Testing (SAST/Container Security and DAST) with a custom Policy Engine that evaluates scan results and enforces security policies before deployment.

---

## Features

- Automated CI/CD using GitHub Actions
- Dockerized Flask web application
- Automated Unit Testing using Pytest
- Container Vulnerability Scanning using Trivy
- Dynamic Application Security Testing using OWASP ZAP
- Custom Policy Engine for security policy enforcement
- Security Dashboard for scan visualization
- Automated Security Report Generation
- Upload of security reports as GitHub Action artifacts
- HTTP Security Headers implementation

---

# Project Architecture

```
                Developer
                     │
               Git Push
                     │
                     ▼
            GitHub Repository
                     │
                     ▼
           GitHub Actions Pipeline
                     │
     ┌───────────────┼────────────────┐
     │               │                │
     ▼               ▼                ▼
 Unit Tests     Docker Build     Trivy Scan
                                        │
                                        ▼
                              Flask Application
                                        │
                                        ▼
                               OWASP ZAP Scan
                                        │
                                        ▼
                                Policy Engine
                                        │
                                        ▼
                              PASS / FAIL Decision
                                        │
                                        ▼
                               Security Reports
                                        │
                                        ▼
                               Security Dashboard
```

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| Framework | Flask |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Unit Testing | Pytest |
| Container Security | Trivy |
| Dynamic Security Testing | OWASP ZAP |
| Version Control | Git |
| Dashboard | HTML, Bootstrap, Jinja2 |

---

# Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
├── reports/
├── scripts/
│   └── policy_engine.py
├── tests/
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```

---

# CI/CD Pipeline Workflow

The pipeline is automatically triggered on every push and pull request to the main branch.

The workflow performs the following stages:

1. Checkout Repository
2. Install Dependencies
3. Execute Unit Tests
4. Build Docker Image
5. Perform Trivy Vulnerability Scan
6. Launch Flask Application
7. Verify Application Health
8. Execute OWASP ZAP Baseline Scan
9. Evaluate Results using Policy Engine
10. Upload Security Reports

---

# Security Scanning

## Trivy

Trivy scans the Docker image for:

- Operating System vulnerabilities
- Application dependencies
- Severity classification
- Fixable vulnerabilities

Output:

```
reports/trivy-report.json
```

---

## OWASP ZAP

OWASP ZAP performs Dynamic Application Security Testing (DAST) against the running application.

The scan detects:

- Missing Security Headers
- Cross-Site Scripting (XSS)
- SQL Injection indicators
- Information Disclosure
- Insecure Configurations

Output:

```
reports/zap-report.json
```

---

# Policy Engine

The custom Policy Engine analyzes both Trivy and OWASP ZAP reports and enforces security policies.

Current Policy Rules:

- Fail if fixable Critical vulnerabilities are detected by Trivy.
- Fail if High Risk alerts are detected by OWASP ZAP.
- Generate a consolidated security summary.

Output:

```
reports/policy-summary.txt
```

---

# Security Dashboard

The dashboard displays:

- Critical Vulnerabilities
- High Vulnerabilities
- Medium Vulnerabilities
- Low Vulnerabilities
- ZAP Alert Summary
- Overall Security Status

---

# Running the Project Locally

## Clone Repository

```bash
git clone https://github.com/ABISHEKKARTHA/automated-devsecops-pipeline.git
cd automated-devsecops-pipeline
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python run.py
```

The application will be available at:

```
http://localhost:5000
```

---

# Docker

Build Docker image

```bash
docker build -t devsecops-pipeline .
```

Run Docker container

```bash
docker run -d -p 5000:5000 devsecops-pipeline
```

---

# GitHub Actions

The GitHub Actions workflow automatically performs:

- Build
- Test
- Security Scan
- Policy Validation
- Artifact Upload

The workflow fails whenever the defined security policy is violated.

---

# Reports

Generated reports include:

```
reports/
├── trivy-report.json
├── zap-report.json
└── policy-summary.txt
```

---

# Future Enhancements

- Kubernetes deployment
- Helm Charts
- GitOps using Argo CD
- Slack / Microsoft Teams notifications
- Terraform Infrastructure Provisioning
- SonarQube Code Quality Analysis
- Dependency Auto-Remediation
- Security Trend Dashboard
- Multi-environment Deployment (Dev / QA / Production)

---

# Screenshots

Include screenshots of:

- GitHub Actions Pipeline
- Security Dashboard
- Trivy Report
- OWASP ZAP Report
- Policy Engine Output

---

# Author

**Abishek V Kartha**

Master of Computer Applications (Cyber Security)

Amrita Vishwa Vidyapeetham

2025–2026

---

# License

This project is developed for academic and educational purposes.
