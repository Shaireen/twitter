from bottle import delete, response
import g




@delete("/api-delete-tweet/<tweet_id>")
def _(tweet_id):
  print(g.TWEETS)
  # Validate that the tweet_id is a valid UUID4
  for index, tweet in enumerate(g.TWEETS):
    if tweet_id == tweet["id"]:
      g.TWEETS.pop(index)
      print(g.TWEETS)
      print(len(g.TWEETS))
      return "tweet deleted"

  response.status = 204
  return "tweet not found"
