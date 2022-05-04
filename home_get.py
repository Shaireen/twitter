from bottle import run, get, view, request, redirect, response
import g
import jwt

@get("/home")
@view("home")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_session_id = request.get_cookie("user_session_id")
    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    user = g.SESSIONS[user_session_id]
    decoded_user = jwt.decode(user, "yes super key", algorithms=["HS256"]) 
    user_pic = decoded_user["pic"]
    user_name = decoded_user["name"]
    user_firstname = decoded_user["firstname"]
    user_lastname = decoded_user["lastname"]
    user_display_info = {
        "src": user_pic, 
        "user_firstname": user_firstname, 
        "user_lastname": user_lastname, 
        "user_name": user_name 
    }
    return dict(tabs=g.TABS, tweets=g.TWEETS, trends=g.TRENDS, items=g.ITEMS, user=user, user_display_info=user_display_info)

