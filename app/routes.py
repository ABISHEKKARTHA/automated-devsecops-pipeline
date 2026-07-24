from flask import jsonify, current_app
from app.services.security_service import get_security_summary
from datetime import datetime
from app.services.zap_service import ZapService
from flask import render_template


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "project": current_app.config["APP_NAME"],
            "description": current_app.config["DESCRIPTION"],
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
            "application": current_app.config["APP_NAME"],
            "version": current_app.config["VERSION"],
            "environment": current_app.config["ENVIRONMENT"],
            "author": current_app.config["AUTHOR"]
        })

    @app.route("/api/info")
    def info():
        return jsonify({
            "application": current_app.config["APP_NAME"],
            "description": current_app.config["DESCRIPTION"],
            "framework": "Flask",
            "containerized": True,
            "pipeline": "GitHub Actions",
            "environment": current_app.config["ENVIRONMENT"]
        })

    @app.route("/api/security")
    def security():
        return jsonify(current_app.config["SECURITY"])

    @app.route("/api/system")
    def system():
        return jsonify({
            "application": current_app.config["APP_NAME"],
            "version": current_app.config["VERSION"],
            "environment": current_app.config["ENVIRONMENT"],
            "python_version": "3.12",
            "docker": True,
            "build_status": "Success",
            "health": "Healthy"
        })

    @app.route("/api/security/report")
    def security_report():

        return get_security_summary()

    @app.route("/dashboard")
    def dashboard():

        data = get_security_summary()
        zap = ZapService.get_summary()

        return render_template(
            "dashboard.html",
            data=data,
            zap=zap
        )