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

@bp.route("/create/step/1", methods=["GET", "POST"])
@requires_login
def create_page_step_1():
    return DashBoardController.create_page_step_1()

# /page/----- para acciones realcionadas con las páginas
@bp.get("/page/edit/<page_id>")
@requires_login
def change_visibility (page_id):
    print(type(page_id))
    return DashBoardController.change_visibility(page_id)
