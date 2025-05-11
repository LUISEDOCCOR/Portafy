from flask import render_template

class PagesController:
    @classmethod
    def home_page (cls):
        return render_template("/pages/index.html")
