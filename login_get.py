from bottle import error, get, request, view

@get("/login")
@view("login")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  return dict(error=error, user_email = user_email)