import bcrypt
from email_validator import validate_email, EmailNotValidError

def check_pw(password_hash, user_password):
    return bcrypt.checkpw(user_password.encode("utf-8"), password_hash)

def check_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def check_password_validity(password):
    return password and len(password) >= 6
