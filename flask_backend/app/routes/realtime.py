from flask import Response, stream_with_context
from flask_smorest import Blueprint
from flask.views import MethodView
import time
import json

blp = Blueprint(
    "Realtime",
    "realtime",
    url_prefix="/realtime",
    description="Endpoints for real-time or polling data."
)

def generate_stream():
    """Yields simple events for demonstration (SSE format)."""
    for i in range(10):
        update = {"timestamp": time.time(), "value": i + 1}
        yield f"data: {json.dumps(update)}\n\n"
        time.sleep(1)

@blp.route("/stream")
class RealtimeStreamView(MethodView):
    """
    PUBLIC_INTERFACE
    GET endpoint that streams real-time data using Server-Sent Events (SSE).
    Returns: Streamed event source content.
    """
    def get(self):
        response = Response(
            stream_with_context(generate_stream()),
            mimetype="text/event-stream"
        )
        response.headers["Cache-Control"] = "no-cache"
        return response
