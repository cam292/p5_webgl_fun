from flask import Blueprint, render_template, current_app


hello_blueprint = Blueprint('hello', __name__, template_folder='templates')


@hello_blueprint.route('/')
@hello_blueprint.route('/<name>')
def hello(name=None):
    current_app.logger.info("Name provided was: {}".format(name))
    return render_template('hello.html', name=name)
