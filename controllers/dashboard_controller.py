from flask import render_template, session

class DashBoardController:
    @classmethod
    def global_variables (cls):
        return {
            "user_email": session["user_email"],
            "user_id": session["user_id"]
        }

    @classmethod
    def home_page(cls):
        return render_template("/pages/dashboard/index.html")
