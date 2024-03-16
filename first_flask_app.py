from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# Using datetime for getting the system datetime when the entry is updated/created
# on the website
from datetime import datetime

# creating the application
app = Flask(__name__)
# Added Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize the Database
db = SQLAlchemy(app)

# Creating the database model -> It stores the schema of the database
class Users(db.Model):
    id = db.Column(db.Integer, primary_Key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True)
    date_added = db.Column(db.Datetime, default = datetime.utcnow) #taking the time of record creation by default


# creating a index route to avoid getting 404 while browsing using app.route() decorator
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)