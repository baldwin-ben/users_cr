# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# Our class user which takes in the databases table in order. Model it after your table.

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# Now we use class methods to query our database
# class method that gets all users in our db. This class method is called in our home page.

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of users
        all_users = []
        # Iterate over the db results and create instances of users with cls.
        for users in results:
            all_users.append( cls(users) )
        return all_users

# class method get_one is linked to the show_user and edit user in my server.py

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('users_schema').query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        return False

# edits all the specified users info. Used in my users/int:id/submit method, edit_user.

    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

# query that is used to create user in my create_user method.

    @classmethod
    def create_user (cls, data):
        query = "INSERT INTO users ( first_name , last_name , email) VALUES ( %(first_name)s , %(last_name)s , %(email)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db(query,data)

# deletes selected user. Used in delete_user method.

    @classmethod
    def delete_user (cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database