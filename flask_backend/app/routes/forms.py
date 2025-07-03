from flask_smorest import Blueprint, abort
from flask.views import MethodView
from marshmallow import Schema, fields, validate

blp = Blueprint(
    "Forms",
    "forms",
    url_prefix="/forms",
    description="Endpoint for dynamic form submissions."
)

class FormSubmissionSchema(Schema):
    """Schema for validating input data for form submission."""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100), description="User name")
    email = fields.Email(required=True, description="User email address")
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "user", "viewer"]), description="Role selection")
    feedback = fields.Str(required=False, allow_none=True, description="Optional feedback or comments")

class SubmissionResponseSchema(Schema):
    """Schema for the response after submission."""
    status = fields.Str(description="Status of the submission")
    message = fields.Str(description="Detailed message about the form submission")
    errors = fields.Dict(keys=fields.Str(), values=fields.List(fields.Str()), description="Validation errors", allow_none=True)

@blp.route("/submit")
class FormSubmitView(MethodView):
    """
    PUBLIC_INTERFACE
    POST endpoint for dynamic form submission.
    Body: {name, email, role, feedback}
    """
    @blp.arguments(FormSubmissionSchema)
    @blp.response(200, SubmissionResponseSchema)
    def post(self, form_data):
        try:
            # Here, save form_data to DB or process as needed
            return {
                "status": "success",
                "message": "Form submission received!",
                "errors": None
            }
        except Exception as e:
            abort(
                500,
                message="Internal server error during form submission",
                errors=str(e)
            )
