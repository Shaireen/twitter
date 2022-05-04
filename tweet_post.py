from bottle import  post, request, response
import uuid
import jwt
import g
import re
import os
import imghdr
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
  tweet_id = str(uuid.uuid4())
  current_date = datetime.now()
  tweet_text = request.forms.get("tweet_text", "")
  if len(tweet_text) < 1 or len(tweet_text) > 100:
    response.status = 400
    return "tweet_text invalid" 
   
  if request.files.get("tweet_image"): 
    image = request.files.get("tweet_image")
    print( dir(image) )
    print(image.filename)
    file_name, file_extension = os.path.splitext(image.filename) # .png .jpeg .zip .mp4
    print(file_name)
    print(file_extension)
      
    # Validate extension
    if file_extension not in (".png", ".jpeg", ".jpg"):
        response.status = 400
        return "image not allowed"
      
    # overwrite jpg to jpeg so imghdr will pass validation
    file_extension = ".jpeg"

    image_id = str(uuid.uuid4())
    # Create new image name
    image_name = f"{file_name}{file_extension}"
    print(image_name)
    # Save the image
    image.save(f"images/{image_name}")

    # Make sure that the image is actually a valid image
    # by reading its mime type
    print("imghdr.what", imghdr.what(f"images/{image_name}"))   # imghdr.what png
    print("file_extension", file_extension)                     # file_extension .png
    imghdr_extension = imghdr.what(f"images/{image_name}")
    if imghdr_extension not in ("png", "jpeg", "jpg"):
        response.status = 400
        print("mmm... suspicious ... it is not really an image")
        # remove the invalid image from the folder
        os.remove(f"images/{image_name}")
        return "mmm... got you! It was not an image"
    tweet = { "id":tweet_id, 
            "user_id": user_id,
            "src": user_pic, 
            "user_firstname": user_firstname, 
            "user_lastname": user_lastname, 
            "user_name": user_name, 
            "text":tweet_text,
            "image":image_name,
            "created_at": current_date.strftime("%m/%d/%Y, %H:%M:%S")
            }

  if not request.files.get("tweet_image"): 
    tweet = { "id":tweet_id, 
            "user_id": user_id,
            "src": user_pic, 
            "user_firstname": user_firstname, 
            "user_lastname": user_lastname, 
            "user_name": user_name, 
            "text":tweet_text,
            "created_at": current_date.strftime("%m/%d/%Y, %H:%M:%S")
            }
  print(tweet)
  g.TWEETS.append(tweet) 
  # Respond
  return tweet_id