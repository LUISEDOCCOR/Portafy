from flask import Blueprint
from controllers.auth_controller import AuthController

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/", methods=["GET", "POST"])
def auth ():
    return AuthController.auth()

@bp.get("/logout")
def logout ():
    return AuthController.logout()
