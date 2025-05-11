from flask import render_template, request, flash, session, redirect, url_for
from models.user_model import UserModel
from utils import check_pw, check_email, check_password_validity

class AuthController:
    @classmethod
    def auth (cls):
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            if not check_email(email) or not check_password_validity(password):
                flash("El correo es inválido o la contraseña es muy corta (min 6 carácteres).")
                return render_template("pages/auth.html")
            try:
                user = UserModel.getByEmail(email)
                if user:
                    if check_pw(user["password"], password):
                        session["user_email"] = email
                        session["user_id"] = str(user["_id"])
                        return redirect(url_for("dashboard.home_page"))
                    else:
                        flash("Datos incorrectos")
                else:
                    new_user_id = UserModel.create(email, password)
                    session["user_email"] = email
                    session["user_id"] = str(new_user_id)
                    return redirect(url_for("dashboard.home_page"))
            except:
                flash("Hubo un error de nuestra parte; intenta más tarde.")
        return render_template("pages/auth.html")

    @classmethod
    def logout(cls):
        session.clear()
        return redirect(url_for("pages.home_page"))
