from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    with app.app_context():
        db.create_all()

    from routes import auth_bp
    app.register_blueprint(auth_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)