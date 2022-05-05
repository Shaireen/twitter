from bottle import error, default_app, delete, get, post, request, response, run, static_file, view
import uuid
import imghdr
import os
import jwt


import g
import signup_post
import signup_get
import home_get
import login_post
import login_get
import logout_get
import tweets_get
import userinfo_get
import tweet_update
import followuser_post
import unfollowuser_delete
import showuserprofile_get
import usertweets_get
import tweet_post
import tweet_delete


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


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")


