from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

blp = Blueprint(
    "Dashboard",
    "dashboard",
    url_prefix="/dashboard",
    description="Endpoints for dashboard data."
)

class DashboardDataSchema(Schema):
    """Schema for dashboard response data."""
    chart_data = fields.List(fields.Dict(), required=True, description="Chart data for dashboard")
    stats = fields.Dict(keys=fields.Str(), values=fields.Float(), required=True, description="Statistics for dashboard")
    message = fields.Str(description="General response message")

@blp.route("/")
class DashboardView(MethodView):
    """
    PUBLIC_INTERFACE
    GET endpoint to fetch dashboard data.
    Returns: Chart data, stats, and status message.
    """
    @blp.response(200, DashboardDataSchema)
    def get(self):
        # Dummy data; replace with real data fetching logic
        data = {
            "chart_data": [
                {"label": "A", "value": 42},
                {"label": "B", "value": 37}
            ],
            "stats": {"total_users": 120, "active_sessions": 15},
            "message": "Dashboard data retrieved successfully"
        }
        return data
