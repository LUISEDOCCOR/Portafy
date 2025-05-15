from flask import render_template, session, redirect, url_for
from models.page_model import PageModel

class PagesController:
    @classmethod
    def home_page (cls):
        # if ("user_id" in session and "user_email" in session ):
        #     return redirect(url_for("dashboard.home_page"))
        return render_template("/pages/index.html")

    @classmethod
    def user_page(cls, url):
        page = PageModel.get_by_url(url)
        if not page:
            return redirect(url_for("pages.home_page"))
        return render_template("/pages/user_page.html", page=page)
