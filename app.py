from bottle import default_app, delete, get, post, request, response, run, static_file, view
import uuid


##############################
tabs = [
  {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home"},
  {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
  {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
  {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
  {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
  {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
  {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
  {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
]

people = [
  {"src": "stephie.png", "name": "Stephie Jensen", "handle": "@sjensen"},
  {"src": "monk.jpg", "name": "Adrian Monk", "handle": "@detective :)"},
  {"src": "kevin.jpg", "name": "Kevin Hart", "handle": "@miniRock"}
]

trends = [
  {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
  {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "20k"},
  {"category": "Russia", "title": "Russia", "tweets_counter": "10k"},
]

tweets = [
  {"id":"1", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"2", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"3", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"id":"4", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"5", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"6", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"id":"7", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"8", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"9", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"id":"10", "src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"id":"11", "src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"id":"12", "src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
]

items = [
  {"img":"bbc.png", "title":"BBC News", "user_name":"bbcworld"},
  {"img":"biden.jpg", "title":"Joe Biden", "user_name":"joebiden"},
  {"img":"harris.jpg", "title":"Vice President", "user_name":"vp"},
]



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
  return dict(tabs=tabs, tweets=tweets, trends=trends, items=items)

##############################
@delete("/api-delete-tweet/<tweet_id>")
def _(tweet_id):
  # Validate that the tweet_id is a valid UUID4
  for index, tweet in enumerate(tweets):
    if tweet_id == tweet["id"]:
      tweets.pop(index)
      return "tweet deleted"

  response.status = 204
  return "tweet not found"


##############################
@post("/api-create-tweet")
def _():
  # Validate
  tweet_text = request.forms.get("tweet_text", "")
  if len(tweet_text) < 1 or len(tweet_text) > 100:
    response.status = 400
    return "tweet_text invalid" 
  # Connect to the db
  # Query
  tweet_id = str(uuid.uuid4())
  tweet = { "id":tweet_id, 
            "src":"6.jpg", 
            "user_first_name":"xxx", 
            "user_last_name":"yyy", 
            "user_name":"xxxyyy", 
            "date":"Feb 20", 
            "text":tweet_text
            }
  tweets.append(tweet)
  # Respond
  return tweet_id


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3000, debug=True, reloader=True, server="paste")
