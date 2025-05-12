from flask import render_template, session

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
    def create_page(cls):
        return render_template("/pages/dashboard/create.html")
