from bottle import run, get, view, request, redirect, response
import g

@get("/home")
@view("home")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_session_id = request.get_cookie("user_session_id")
    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    user = g.SESSIONS[user_session_id]
    return dict(tabs=g.TABS, tweets=g.TWEETS, trends=g.TRENDS, items=g.ITEMS, user=user)

