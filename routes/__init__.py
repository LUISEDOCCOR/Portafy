from .auth_routes import bp as bp_auth

def register_routes(app):
    app.register_blueprint(bp_auth)
