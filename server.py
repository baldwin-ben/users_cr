from flask import Flask, render_template, request, redirect
# import the class from user.py
from user_model import User
app = Flask(__name__)

# Home page route. Renders home page

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users) #users has to match what is in jinja in order for your page to load the data.

# route used to render create.html file

@app.route("/users/new")
def new_user_form():
    return render_template("create.html")

# route that redirects you to the users page once it has been created.

@app.route("/users/create", methods = ['POST'])
def create_user():
    id = User.create_user(request.form)
    return redirect(f"/users/{id}")

#rendering edit_user form specified in return statement

@app.route("/users/<int:id>/edit")
def edit_user_id(id):
    data = {"id":id}
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)

# submitting the new user to database. Connected to @classmethod edit.
# id is specified in url and passed into data dictionary.
# in the data dictionary we supply what data we want to update.
@app.route("/users/<int:id>/submit", methods = ['POST'])
def edit_user(id):
    data = {'id':id,
    'first_name': request.form["first_name"],
    'last_name': request.form["last_name"],
    'email': request.form["email"]
    }
    User.edit(data)
    return redirect("/")

# route that shows the selected users information.
# this route is connected to my get one user class.

@app.route("/users/<int:id>")
def show_user(id):
    data = {'id':id}
    this_user = User.get_one(data) # this calls the classmethod get_one from our user model
    return render_template("read_one.html", user=this_user)

# route that deletes the selected user

@app.route("/users/delete/<int:id>")
def delete_user(id):
    data = {'id':id}
    User.delete_user(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)