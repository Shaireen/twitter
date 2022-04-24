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

@get("/login")
@view("login")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  return dict(error=error, user_email = user_email)

##############################

@get("/signup")
@view("index")
def _():
  error = request.params.get("error")
  user_email = request.params.get("user_email")
  user_name = request.params.get("user_name")
  user_firstname = request.params.get("user_firstname")
  user_lastname = request.params.get("user_lastname")
  return dict(error=error, user_email = user_email, user_name = user_name, user_firstname = user_firstname, user_lastname = user_lastname)


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")
