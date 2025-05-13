from flask import render_template, session, request, flash
import re

class DashBoardController:
    @classmethod
    def global_variables (cls):
        return {
            "user_email": session["user_email"],
            "user_id": session["user_id"],
            "pages": []
        }

    @classmethod
    def home_page(cls):
        return render_template("/pages/dashboard/index.html")

    @classmethod
    def create_page_step_1(cls):
        path_template = "/pages/dashboard/create_step_1.html"
        if request.method == "POST":
            page_title = request.form.get("page_title")
            page_desc = request.form.get("page_desc")
            user_shortBio = request.form.get("user_shortBio")
            user_name = request.form.get("user_name")
            page_url = request.form.get("page_url")

            if not page_title or not page_desc or not user_shortBio or not user_name or not page_url:
                flash("Todos los campos son necesarios")
                return render_template(path_template)

            if not page_url.isalpha() or re.search(r"\s", page_url):
                flash("La url no puede contener espacios ni caracteres especiales.")
                return render_template(path_template)



        return render_template(path_template)
