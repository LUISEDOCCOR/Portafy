from flask import Flask, render_template
from routes.auth_routes import bp as bp_auth

app = Flask(__name__)
app.register_blueprint(bp_auth)

@app.get("/")
def index():
    return render_template('/pages/index.html')
