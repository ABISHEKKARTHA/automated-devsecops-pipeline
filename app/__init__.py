from flask import Flask
from .config import Config
from .routes import register_routes


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    register_routes(app)

    @app.after_request
    def add_security_headers(response):
        # Prevent MIME type sniffing
        response.headers["X-Content-Type-Options"] = "nosniff"

        # Prevent clickjacking
        response.headers["X-Frame-Options"] = "DENY"

        # Restrict resource loading
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "style-src 'self' https://cdn.jsdelivr.net; "
            "script-src 'self'; "
            "img-src 'self' data:;"
        )

        # Disable unnecessary browser features
        response.headers["Permissions-Policy"] = (
            "geolocation=(), microphone=(), camera=()"
        )

        # Restrict cross-origin resource usage for enhanced security
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"

        # Control referrer information
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

        return response

    return app