from flask import Flask, render_template, request, redirect
# import the class from user.py
from user_model import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users) #users has to match what is in jinja in order for your page to load the data.


@app.route("/user/new")
def new_user_form():
    return render_template("create.html")

@app.route("/user/create", methods = ['POST'])
def create_user():
    User.create_user(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)