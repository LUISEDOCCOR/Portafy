from database.mongo import db

class UserModel ():
    @classmethod
    def getByEmail(cls, email):
        return db.users.find_one({"email": email})
