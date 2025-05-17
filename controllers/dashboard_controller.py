from flask import render_template, session, request, flash, redirect, url_for
import re
from bson import ObjectId
from models.page_model import PageModel

class DashBoardController:
    @classmethod
    def global_variables (cls):
        return {
            "user_email": session["user_email"],
            "user_id": session["user_id"],
            "pages": PageModel.get_by_user_id(ObjectId(session["user_id"]))
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

            try:
                if PageModel.get_by_url(page_url):
                    flash("Ya existe una página con esa URL")
                    return render_template(path_template)

                page_id = PageModel.create_page({
                    "page_title": page_title,
                    "page_desc": page_desc,
                    "user_shortBio": user_shortBio,
                    "user_name": user_name,
                    "page_url": page_url,
                    "isPublic": True,
                    "user_id": ObjectId(session["user_id"])
                })

                return redirect(url_for("dashboard.home_page"))
                # cambiar al siguente paso, y guardar el id de la pagina

            except:
                flash("Hubo un error de nuestra parte; intenta más tarde.")

        return render_template(path_template)

    @classmethod
    def change_visibility(cls, page_id):
        try:
            page = PageModel.get_by_id(ObjectId(page_id))
            if str(page["user_id"]) != session["user_id"]:
                flash("El ID pertenece a una página que no es tuya")
                return redirect(url_for("dashboard.home_page"))
            PageModel.change_visibility(page["_id"], not page["isPublic"])
            return redirect(url_for("dashboard.home_page"))
        except:
            flash("Hubo un error")
            return redirect(url_for("dashboard.home_page"))
