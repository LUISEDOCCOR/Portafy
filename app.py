import os
from flask import Flask
from routes import register_routes
from dotenv import load_dotenv

def create_app ():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    register_routes(app)
    return app
