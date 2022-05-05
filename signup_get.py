from bottle import get, request, view

@get("/signup")
@view("index")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  user_name = request.params.get("user_name")
  user_firstname = request.params.get("user_firstname")
  user_lastname = request.params.get("user_lastname")
  return dict(error=error, user_email = user_email, user_name = user_name, user_firstname = user_firstname, user_lastname = user_lastname)