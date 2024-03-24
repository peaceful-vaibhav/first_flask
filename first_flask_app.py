from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from img_to_binary import to_binary
from datacrud import insert_data, fetch_data
# Using datetime for getting the system datetime when the entry is updated/created
# on the website
from datetime import datetime, timezone

# creating the application
app = Flask(__name__)
# Added Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize the Database
db = SQLAlchemy(app)

app.app_context().push()

# Creating the database model -> It stores the schema of the database
# class test(db.Model):
#     id = db.Column(db.Integer, primary_Key = True)
#     name = db.Column(db.String(50), nullable = False)
#     email = db.Column(db.String(50), unique = True)
#     date_added = db.Column(db.DateTime, default = datetime.utcnow) #taking the time of record creation by default

class test_schema(db.Model):
    id = db.Column(db.String(50), primary_key = True, nullable = False)
    date_added = db.Column(db.DateTime, default = datetime.now(timezone.utc), primary_key = True)
    image_file = db.Column(db.BLOB, nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.id

# creating a index route to avoid getting 404 while browsing using app.route() decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_image', methods = ['POST'])
def insert_image():
    if request.method == "POST":
        uploaded = request.files['img']
        print(f"uploaded: {uploaded}")

        # blob_img = image.read()

        uploaded_blob = to_binary(uploaded)

        inserted = insert_data(filename=uploaded.filename, blob_data=uploaded_blob)

        if inserted == "created":
            insert_data(filename=uploaded.filename, blob_data=uploaded_blob)
        
        data = fetch_data(filename=uploaded.filename)

        return f"Uploaded: {uploaded.filename}"
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)