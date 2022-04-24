from bottle import put, response
import g
from datetime import datetime 

@put("/api-update-tweet/<tweet_id>/<tweet_text>")
def _(tweet_id, tweet_text):
    if len(tweet_text) < 1 or len(tweet_text) > 100:
        response.status = 400
        return "tweet_text invalid" 
    for index, tweet in enumerate(g.TWEETS):
        if tweet_id == tweet["id"]:
            g.TWEETS[index]["text"] = tweet_text
            current_date = datetime.now()
            g.TWEETS[index]["updated_at"] = current_date.strftime("%m/%d/%Y, %H:%M:%S")
            print(g.TWEETS)
            return "tweet updated"
    response.status = 204
    return "tweet not found"
