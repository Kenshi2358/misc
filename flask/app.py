"""
To run this script, cd to this directory in a terminal and type: flask run
Then open a browser to URL: http://localhost:5000

To change the port, type: flask run -p 3000
Then go to URL: http://localhost:3000

Can get to the 2nd page by going to: http://localhost:3000/page2

Ctrl+C to quit the flask application.

Flask is a web framework that allows developers to build lightweight web applications quickly.

Flask Blueprints encapsulate functionality, such as views, templates, and other resources.
A blueprint is a flask class.
A blueprint is an object that allows defining application functions
without requiring an application object ahead of time.

Flask does not enforce any particular project layout.
The writer decides how to organize the layout.
"""

from flask import Flask

# To use any flask blueprint, you have to import the blueprint.
# and then register it in the application using register_blueprint().
# When a flask blueprint is registered, the application is extended with its contents.
from ex_blueprint import ex_blueprint

app = Flask(__name__)
app.register_blueprint(ex_blueprint)

# @app.route('/')
# def index():
#     return "This is an example app"
