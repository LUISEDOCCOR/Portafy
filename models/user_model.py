from database.mongo import db
import bcrypt

class UserModel ():
    @classmethod
    def getByEmail(cls, email):
        return db.users.find_one({"email": email})

    @classmethod
    def create(cls, email, password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return db.users.insert_one({"email": email, "password": password_hash}).inserted_id
