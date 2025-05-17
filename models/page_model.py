from database.mongo import db

class PageModel:
    @classmethod
    def create_page(cls, data):
        return db.pages.insert_one(data).inserted_id

    @classmethod
    def get_by_url(cls, url):
        return db.pages.find_one({"page_url": url})

    @classmethod
    def get_by_user_id (cls, user_id):
        return list(db.pages.find({"user_id": user_id}))

    @classmethod
    def get_by_id(cls, id):
        return db.pages.find_one({"_id": id})

    @classmethod
    def change_visibility (cls, id, value):
        db.pages.update_one({"_id": id}, {"$set": {"isPublic": value}})
