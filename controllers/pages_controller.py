from flask import render_template, session, redirect, url_for

class PagesController:
    @classmethod
    def home_page (cls):
        if ("user_id" in session and "user_email" in session ):
            return redirect(url_for("dashboard.home_page"))
        return render_template("/pages/index.html")
