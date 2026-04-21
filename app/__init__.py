import os
from flask import Flask

def create_app():
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="static",
    )

    # Ensure folders exist
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs/warehouse", exist_ok=True)
    os.makedirs("outputs/feature_store", exist_ok=True)
    os.makedirs("outputs/secure_raw", exist_ok=True)
    os.makedirs("outputs/research", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
