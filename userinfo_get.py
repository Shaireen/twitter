from bottle import get, request
import g
import jwt

@get("/user-info")
def _():
    user_session_id = request.get_cookie("user_session_id")
    user_info = jwt.decode(g.SESSIONS[user_session_id], "yes super key", algorithms=["HS256"]) 
    return dict(user_info = user_info)