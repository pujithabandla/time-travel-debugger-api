from flask import Flask
from models.event import db
from routes.event_routes import event_bp
import os

app = Flask(__name__)

DB_PATH = os.path.join("/tmp", "events.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(event_bp)

@app.route("/")
def home():
    return {"message": "Time Travel Debugger API running"}

# 🔥 CREATE TABLES ON STARTUP
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)