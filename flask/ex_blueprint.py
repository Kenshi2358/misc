from flask import Blueprint

# The 1st argument: 'ex_blueprint' is the blueprint's name.
# The 2nd argument __name__, is the blueprint's import name.
# Flask uses this to locate the blueprints resources.

ex_blueprint = Blueprint('ex_blueprint', __name__)

# Route is a decorator that allows you to associate a view function to a URL route.
@ex_blueprint.route('/')
def index():
    return "This is an example app"