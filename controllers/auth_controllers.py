from flask import render_template

class AuthController:
    @classmethod
    def auth (cls):
        return render_template("pages/auth.html")
