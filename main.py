from flask import Flask, render_template, request
import smtplib
import requests

gmail = "testpython63@gmail.com"
password = "Jerapotamo29"
yahoo = "testpython76@yahoo.com"

response = requests.get("https://api.npoint.io/a107b8ae6f9c97c2cb30").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=response)

@app.route("/index.html")
def main_page():
    data = response
    return render_template("index.html", data=data)

@app.route("/about.html")
def about_page():
    return render_template("about.html")

@app.route("/<int:index>")
def post_page(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact.html", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        send_email(request.form["name"], request.form["email"], request.form["phone"], request.form["message"])
        return render_template("contact.html", valid_access=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Name: {name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(gmail, password)
            connection.sendmail(from_addr=gmail, to_addrs=gmail, msg=email_message)

if __name__ == "__main__":
    app.run(debug=True)
