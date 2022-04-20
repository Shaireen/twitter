from bottle import get
import g

@get("/user-profile-info/<user_id>")
def _(user_id):
    for index, item in enumerate(g.ITEMS):
        if user_id == item["id"]:
            item = item
            print(item)
            return item
    response.status = 404
    return

