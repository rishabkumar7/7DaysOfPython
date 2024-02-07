# Day 5 - Web development in Python

Python is quite capable when it comes to web development, and there are a variety of frameworks and modules are available for it. These can be used to create web applications.
Flask, Django, and Pyramid are a few well-known frameworks. The choice of framework will rely on the project's requirements. Each of these frameworks has advantages and disadvantages of its own.

## Creating a basic web app using Flask

Creating a basic web application using Flask: Flask is a micro web framework for Python that is easy to learn and use. It provides a simple way to create web applications and APIs using Python. Here are some examples of Flask code for creating a basic web application:

``` python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' 
```
This code creates a Flask application and defines a single route for the root URL (/). When the user visits the URL, the hello_world() function is called and returns the string 'Hello, World!'.

## Working with databases

The majority of online applications need some sort of permanent storage, and Python offers a number of modules and frameworks for doing so. Popular options include Django ORM, Peewee, and SQLAlchemy. Here is an illustration of how to work with a SQLite database using SQLAlchemy:

``` python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
```

This code creates a SQLite database and a User table using SQLAlchemy. The index() function queries the database for all users and passes them to the template for rendering.

Having a good understanding of how these web apps work, will help you with automation and deployment when it comes to practicing DevOps.
You can dive deeper into how you can build APIs using Python and serverless technologies like [AWS Lambda](https://aws.amazon.com/lambda/), [Azure Functions](https://azure.microsoft.com/en-ca/products/functions#:~:text=Azure%20Functions%20is%20an%20event,highest%20level%20of%20hardware%20abstraction.) etc.

I have a demo on [how I built a serverless resume API](https://github.com/rishabkumar7/AzureResumeAPI).

## Building APIs in Python

Creating an API (Application Programming Interface) in Python can be a straightforward process, thanks to various frameworks and libraries available. Three popular methods to set up a web API in Python: Flask, FastAPI, and Django Rest Framework.

In the following video, I showcase all three of them:
<iframe width="700" height="400" src="https://www.youtube.com/embed/k8eu2QDikIc?si=ynwIjeR3ruC5LVhs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
