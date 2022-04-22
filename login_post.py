from bottle import  post, request, redirect, response
import uuid
import jwt
import g


@post("/login")
def _():
    user_email =  request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    users = request.get_cookie("users", secret=g.COOKIE_SECRET)
    for user in users:
        user = jwt.decode(user, "yes super key", algorithms=["HS256"]) 
        print(user)
        
        if user_email == user["email"] and user_password == user["password"]:
            user_session_id = str(uuid.uuid4())
            encoded_user = jwt.encode(user, "yes super key", algorithm="HS256")
            g.SESSIONS[user_session_id] = encoded_user
            print(g.SESSIONS)
            response.set_cookie("user_session_id", user_session_id)
            return redirect("/home")
        if user_email == user["email"] and user_password != user["password"]:
            response.status = 400
            return redirect(f"/login?error=user_password&user_email={user_email}")
        if user_password == user["password"] and user_email != user["email"]:
            response.status = 400
            return redirect(f"/login?error=user_email")
    response.status = 404
    return redirect("/login")
