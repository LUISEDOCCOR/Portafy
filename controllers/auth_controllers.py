from flask import render_template
from models.user_model import UserModel

class AuthController:
    def auth (self):
        print(UserModel.getByEmail("Luis"))
        return render_template("pages/auth.html")
