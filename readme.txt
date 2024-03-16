What is Flask ?
- Flask is a back-end web application development framework based on Python

How to make an application using Flask ?
- We start by the development of a Flask application instance and over there we need to use the special attribute "__name__"
- The main purpose of using this attribute is to fetch the name of the location where all the resources, templates and files would
be present.
Let's say, if the Flask Application is running interactively (if the program is running in the main program), then all the files will
be present in the working directory only and we will be needing the working directory name for reference to start navigating to
the templates folder and to the static folder for finding files like index.html

In this case, __name__ == "__main__"

Now, in the case when this application will be imported as a module into the main program, then the name of the working directory
where main/top-level environment will run would be different than where the templates and static files will actually be present.

The actual files Flask Application files will then be present under the module named folder which would have been imported
and then that name will be required.

In this case, __name__ == "parent_package_path.module_name"

Sources: 
https://docs.python.org/3/library/__main__.html -> The starting part will be sufficient to read and understand the same.
https://teamtreehouse.com/community/can-someone-help-me-understand-flaskname-a-little-better -> Answer to this exact question.


After instantiation of the app, we create a route for the app.

What is a route ?
- It is a mapping of the URL with a function or a code snippet to be rendered/depicted on the webserver.
In Flask, we use @app.route() decorator to indicate that the function is bound/mapped with the URL provided in the parameter
of the route function.


------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------

Now, that we have developed the app with the fixed information. If we want to have a Flask Application with "Static" content, then
we need to add template rendering functionality in our Application using Flask Module's class called "Render_Template".

Now, we have utilized the Jinja template used by Flask to create the HTML templates over here.
-- base.html -> it will store the basic boiler plate code for all the content of the website
-- index.html -> this contains the code above the base.html file, not the whole content but the additions over the base.html

After this, we create the static content to be used in the website, like the margins and the font size using CSS.

------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------

After making the template and setting the styling for the web app content, we now need to perform some database connection to
store the required data.

For database setup, we are using Flask_SQLAlchemy as:
    1. We are defining the application configuration by first setting up the database URI
        --> Note that we are using '///' with the database type (SQLite in our case) because we want to use relative path
        --> To use absolute path, we need to use '////'
    2. 

