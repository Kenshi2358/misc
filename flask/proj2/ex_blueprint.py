from flask import Blueprint, redirect, url_for

# The 1st argument: 'ex_blueprint' is the blueprint's name.
# The 2nd argument __name__, is the blueprint's import name.
# Flask uses this to locate the blueprints resources.

ex_blueprint = Blueprint('ex_blueprint', __name__)


# Route is a decorator that allows you to associate a view function to a URL route.
@ex_blueprint.route('/')
def index():
    return "This is an example app"


# The 1st line is the decorator to route the URL.
# The 2nd line is the binding to the function of route
@ex_blueprint.route('/page2')
def page2():
    return "This is another page of the app"


@ex_blueprint.route('/admin')
def hello_admin():
    return "Hello Admin"


@ex_blueprint.route('/guest/<guest>')
def hello_guest(guest):
    str1 = f'Hello {guest} as Guest'
    return str1


@ex_blueprint.route('/user/<name>')
def hello_user(name):
    # dynamic binding of the URL to a function, example.
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
