from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(300), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)