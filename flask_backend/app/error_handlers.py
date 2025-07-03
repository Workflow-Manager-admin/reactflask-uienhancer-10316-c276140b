from flask import jsonify
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import HTTPException

# PUBLIC_INTERFACE
def register_error_handlers(app):
    """Register centralized error handlers for validation and generic errors in the Flask app."""

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        """Handles Marshmallow validation errors."""
        response = jsonify({
            "status": "error",
            "message": "Validation Failed",
            "errors": err.messages
        })
        response.status_code = 400
        return response

    @app.errorhandler(HTTPException)
    def handle_http_exception(err):
        """Handles standard HTTP errors."""
        response = jsonify({
            "status": "error",
            "message": err.description
        })
        response.status_code = err.code if hasattr(err, "code") else 500
        return response

    @app.errorhandler(Exception)
    def handle_generic_error(err):
        """Handles uncaught errors."""
        response = jsonify({
            "status": "error",
            "message": "Internal Server Error",
            "detail": str(err)
        })
        response.status_code = 500
        return response
