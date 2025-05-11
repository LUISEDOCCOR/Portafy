from flask import redirect, url_for, session
from functools import wraps

def requires_login(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		if ("user_email" not in session and "user_id" not in session):
			return redirect(url_for("pages.home_page"))
		else:
			return f(*args, **kwargs)
	return decorator
