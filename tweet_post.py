from bottle import  post, request, response
import uuid
import jwt
import g
from datetime import datetime

@post("/api-create-tweet")
def _():
  # Validate
  user_session_id = request.get_cookie("user_session_id")
  user = g.SESSIONS[user_session_id]
  decoded_user = jwt.decode(user, "yes super key", algorithms=["HS256"]) 
  user_id = decoded_user["id"]
  user_pic = decoded_user["pic"]
  user_name = decoded_user["name"]
  user_firstname = decoded_user["firstname"]
  user_lastname = decoded_user["lastname"]
  print(user_id)
  tweet_text = request.forms.get("tweet_text", "")
  if len(tweet_text) < 1 or len(tweet_text) > 100:
    response.status = 400
    return "tweet_text invalid" 
  # Connect to the db
  # Query
  tweet_id = str(uuid.uuid4())
  current_date = datetime.now()

  tweet = { "id":tweet_id, 
            "user_id": user_id,
            "src": user_pic, 
            "user_firstname": user_firstname, 
            "user_lastname": user_lastname, 
            "user_name": user_name, 
            "text":tweet_text,
            "created_at": current_date.strftime("%m/%d/%Y, %H:%M:%S")
            }
  g.TWEETS.append(tweet) 
  # Respond
  return tweet_id