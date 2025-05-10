from flask import Flask
from routes import register_routes
from dotenv import load_dotenv

def create_app ():
    load_dotenv()
    app = Flask(__name__)
    register_routes(app)
    return app
