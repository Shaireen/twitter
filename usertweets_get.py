from bottle import get
import g

@get("/user-tweets/<user_id>")
def _(user_id):
    user_tweets = filter(lambda tweet: tweet["user_id"] == user_id, g.TWEETS)
    return dict(tweets = list(user_tweets))

 