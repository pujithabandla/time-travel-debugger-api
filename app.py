from flask import Flask
from models.event import db
from routes.event_routes import event_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(event_bp)

@app.route("/")
def home():
    return {"message": "Time Travel Debugger API running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)