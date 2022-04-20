from bottle import delete, request, response
import g
import jwt

@delete("/unfollow-user/<following_id>")
def _(following_id):
    user_session_id = request.get_cookie("user_session_id")
    decoded_session = jwt.decode(g.SESSIONS[user_session_id], "yes super key", algorithms=["HS256"]) 
    if "following" in decoded_session and following_id in decoded_session["following"]:
        for index, following in enumerate(decoded_session["following"]):
            if following_id == following:
                decoded_session["following"].pop(index)
                print(decoded_session["following"])
                g.SESSIONS[user_session_id] = jwt.encode(decoded_session, "yes super key", algorithm="HS256")
                return "following user deleted"
        response.status = 204
        return "tweet not found"
    return