from bottle import post, request
import g
import jwt

@post("/follow-user/<following_id>")
def _(following_id):
    user_session_id = request.get_cookie("user_session_id")
    decoded_session = jwt.decode(g.SESSIONS[user_session_id], "yes super key", algorithms=["HS256"]) 
    if "following" in decoded_session:
        decoded_session["following"].append(following_id)
    else: decoded_session["following"] = [following_id]
    g.SESSIONS[user_session_id] = jwt.encode(decoded_session, "yes super key", algorithm="HS256")
    print(g.SESSIONS)
    return