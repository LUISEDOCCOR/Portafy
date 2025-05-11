from flask import Blueprint
from decorators.auth_decorator import requires_login
from controllers.dashboard_controller import DashBoardController

bp = Blueprint("dashboard", __name__)

@bp.context_processor
def global_variables():
    return DashBoardController.global_variables()

@bp.get("/home")
@requires_login
def home_page():
    return DashBoardController.home_page()
