from bottle import get
import g

@get("/tweets")
def _(): 
    return dict(tweets=g.TWEETS)