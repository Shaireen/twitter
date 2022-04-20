from bottle import error, default_app, delete, get, post, request, response, run, static_file, view
import uuid
import imghdr
import os
import jwt


import g
import signup_post
import home_get
import login_post
import logout_get
import tweets_get
import userinfo_get
import tweet_update
import followuser_post
import unfollowuser_delete
import showuserprofile_get
import usertweets_get

##############################


##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/app.js")
def _():
  return static_file("app.js", root=".")

##############################
@get("/validator.js")
def _():
  return static_file("validator.js", root=".")

##############################
@get("/images/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images")

##############################
@get("/")
@view("index")
def _():
    error = request.params.get("error")
    return dict(error=error)

@get("/login")
@view("login")
def _():
    return 

@get("/signup")
@view("index")
def _():
  error = request.params.get("error")
  return dict(error=error)

@get("/userpage")
@view("userpage")
def _():
    return dict(tabs=g.TABS, tweets=g.TWEETS, trends=g.TRENDS, items=g.ITEMS)
##############################
@delete("/api-delete-tweet/<tweet_id>")
def _(tweet_id):
  print(g.TWEETS)
  # Validate that the tweet_id is a valid UUID4
  for index, tweet in enumerate(g.TWEETS):
    if tweet_id == tweet["id"]:
      g.TWEETS.pop(index)
      print(g.TWEETS)
      return "tweet deleted"

  response.status = 204
  return "tweet not found"


##############################
@post("/api-create-tweet")
def _():
  # Validate
  user_session_id = request.get_cookie("user_session_id")
  user = g.SESSIONS[user_session_id]
  decoded_user = jwt.decode(user, "yes super key", algorithms=["HS256"]) 
  user_id = decoded_user["id"]
  print(user_id)
  tweet_text = request.forms.get("tweet_text", "")
  if len(tweet_text) < 1 or len(tweet_text) > 100:
    response.status = 400
    return "tweet_text invalid" 
  # Connect to the db
  # Query
  tweet_id = str(uuid.uuid4())
  tweet = { "id":tweet_id, 
            "user_id": user_id,
            "src":"6.jpg", 
            "user_first_name":"xxx", 
            "user_last_name":"yyy", 
            "user_name":"xxxyyy", 
            "date":"Feb 20", 
            "text":tweet_text
            }
  g.TWEETS.append(tweet) 
  # Respond
  return tweet_id


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")
