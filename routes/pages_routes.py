from flask import Blueprint
from controllers.pages_controller import PagesController

bp = Blueprint("pages", __name__)

@bp.get("/")
def home_page():
    return PagesController.home_page()

@bp.get("/<url>")
def user_page(url):
    return PagesController.user_page(url)
