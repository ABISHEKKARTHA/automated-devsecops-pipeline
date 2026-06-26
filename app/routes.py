from flask import jsonify
from datetime import datetime


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "project": "Automated DevSecOps CI/CD Pipeline",
            "message": "Welcome to the DevSecOps API",
            "status": "Running"
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "UP",
            "timestamp": datetime.now().isoformat()
        })

    @app.route("/version")
    def version():
        return jsonify({
            "version": "1.0.0",
            "environment": "Development"
        })

    @app.route("/api/info")
    def info():
        return jsonify({
            "framework": "Flask",
            "containerized": False,
            "pipeline": "GitHub Actions"
        })

    @app.route("/api/security")
    def security():
        return jsonify({
            "trivy": "Pending",
            "owasp_zap": "Pending",
            "policy_engine": "Pending"
        })