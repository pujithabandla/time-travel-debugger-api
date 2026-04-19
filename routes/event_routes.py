from flask import Blueprint, request, jsonify
from models.event import db, Event

event_bp = Blueprint("event_bp", __name__)

# ADD EVENT
@event_bp.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    # SAFE CHECKS 🔥
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "event_type" not in data or "message" not in data:
        return jsonify({"error": "event_type and message required"}), 400

    try:
        event = Event(
            event_type=data["event_type"],
            message=data["message"]
        )

        db.session.add(event)
        db.session.commit()

        return jsonify({"message": "Event stored", "id": event.id})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET ALL EVENTS
@event_bp.route("/events", methods=["GET"])
def get_events():
    try:
        events = Event.query.order_by(Event.timestamp.asc()).all()

        return jsonify([
            {
                "id": e.id,
                "event_type": e.event_type,
                "message": e.message,
                "timestamp": e.timestamp.isoformat()
            } for e in events
        ])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# TIME TRAVEL FEATURE 🔥
@event_bp.route("/timeline/<int:event_id>", methods=["GET"])
def timeline(event_id):
    try:
        target = Event.query.get(event_id)

        if not target:
            return jsonify({"error": "Event not found"}), 404

        all_events = Event.query.order_by(Event.timestamp.asc()).all()

        index = None
        for i, e in enumerate(all_events):
            if e.id == event_id:
                index = i
                break

        start = max(0, index - 2)
        end = min(len(all_events), index + 3)

        surrounding = all_events[start:end]

        return jsonify({
            "target_event": {
                "id": target.id,
                "message": target.message
            },
            "timeline": [
                {
                    "id": e.id,
                    "event_type": e.event_type,
                    "message": e.message
                } for e in surrounding
            ]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500