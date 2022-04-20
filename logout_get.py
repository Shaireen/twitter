from bottle import get, request, redirect
import g

@get("/logout")
def _():
    user_session_id = request.get_cookie("user_session_id")
    g.SESSIONS.pop(user_session_id)
    return redirect("/login")
