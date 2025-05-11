from .auth_routes import bp as bp_auth
from .pages_routes import bp as bp_pages
from .dashboard_routes import bp as bp_dashbaord

def register_routes(app):
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_pages)
    app.register_blueprint(bp_dashbaord)
