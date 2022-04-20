from bottle import run, post, request, redirect, response
import uuid
import jwt
import re
import g 
import os
import imghdr
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@post("/signup")
def _():
    user_id = str(uuid.uuid4())

    

    if not request.forms.get("user_email"):
        response.status = 400
        return redirect("/signup?error=user_email")    
    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return redirect("/signup?error=user_email")

    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
        response.status = 400
        return redirect(f"/signup?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) < 6:
        response.status = 400
        return redirect(f"/signup?error=user_password&user_email={user_email}")
    if len(request.forms.get("user_password")) > 50:
        response.status = 400
        return redirect(f"/signup?error=user_password&user_email={user_email}")

    user_password = request.forms.get("user_password")

    if not request.forms.get("user_name"):
        response.status = 400
        return redirect(f"/signup?error=user_name&user_email={user_email}")
    if len(request.forms.get("user_name")) < 3:
        response.status = 400
        return redirect(f"/signup?error=user_name&user_email={user_email}")
    if len(request.forms.get("user_name")) > 50:
        response.status = 400
        return redirect(f"/signup?error=user_name&user_email={user_email}")

    user_name = request.forms.get("user_name")


    if not request.forms.get("user_firstname"):
        response.status = 400
        return redirect(f"/signup?error=user_firstname&user_email={user_email}")
    if len(request.forms.get("user_firstname")) < 3:
        response.status = 400
        return redirect(f"/signup?error=user_firstname&user_email={user_email}")
    if len(request.forms.get("user_firstname")) > 50:
        response.status = 400
        return redirect(f"/signup?error=user_firstname&user_email={user_email}")
    
    user_firstname = request.forms.get("user_firstname")

    if not request.forms.get("user_lastname"):
        response.status = 400
        return redirect(f"/signup?error=user_lastname&user_email={user_email}")
    if len(request.forms.get("user_lastname")) < 3:
        response.status = 400
        return redirect(f"/signup?error=user_lastname&user_email={user_email}")
    if len(request.forms.get("user_lastname")) > 50:
        response.status = 400
        return redirect(f"/signup?error=user_lastname&user_email={user_email}")

    user_lastname = request.forms.get("user_lastname")

    if not request.files.get("my_image"):
        response.status = 400
        return redirect(f"/signup?error=profile_pic&user_email={user_email}")

    image = request.files.get("my_image")
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
    if file_extension == ".jpg": file_extension = ".jpeg"

    image_id = str(uuid.uuid4())
    # Create new image name
    image_name = f"{user_id}{file_extension}"
    print(image_name)
    # Save the image
    image.save(f"images/{image_name}")

    # Make sure that the image is actually a valid image
    # by reading its mime type
    print("imghdr.what", imghdr.what(f"images/{image_name}"))   # imghdr.what png
    print("file_extension", file_extension)                     # file_extension .png
    imghdr_extension = imghdr.what(f"images/{image_name}")
    if file_extension != f".{imghdr_extension}":
        response.status = 400
        print("mmm... suspicious ... it is not really an image")
        # remove the invalid image from the folder
        os.remove(f"images/{image_name}")
        return "mmm... got you! It was not an image"
    
    user = {"id": user_id, 
    "email": user_email, 
    "name": user_name,
    "firstname": user_firstname,
    "lastname": user_lastname,
    "password": user_password,
    "pic": image_name}
    encoded_jwt = jwt.encode(user, "yes super key", algorithm="HS256")
    g.USERS.append(encoded_jwt)
    response.set_cookie("users", g.USERS, secret=g.COOKIE_SECRET)
    print(g.USERS)
    
    sender_email = "quagganqueen401@gmail.com"
    receiver_email = user_email
    password = g.GMAIL_PASS

    message = MIMEMultipart("alternative")
    message["Subject"] = "My Company"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Thank you.
    """

    html = """\
    <html>
        <body>
        <p>
            Hi,<br>
            <b>How are you?</b><br>
        </p>
        </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        except Exception as ex:
            print("ex")
            return "uppps... could not send the email"




   
    return redirect("/login")