from bottle import put, response,  request
import g

import re
import os
import imghdr
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
            if request.files.get("tweet_edit_image"):
                g.TWEETS[index]["image"] = image_name
            print(g.TWEETS)
            return "tweet updated"
    response.status = 204
    return "tweet not found"
