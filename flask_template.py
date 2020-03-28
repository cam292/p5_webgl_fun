import os

from logging.config import dictConfig
from flask import Flask, render_template
from config import config
from application.hello.hello import hello_blueprint


def create_application():
    """
    Initialize our flask application and the nifi connection it uses.

    :return: The new flask application
    """
    # Setup logging
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG' if os.getenv('DEBUG', False) else 'INFO',
            'handlers': ['wsgi']
        }
    })

    # Initialize the app
    application = Flask(__name__)

    # Secret Key
    application.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(32))

    # Debug
    env = os.getenv('ENVIRONMENT', 'production')
    application.config['ENV'] = env
    application.config['DEBUG'] = os.getenv('DEBUG', config[env]['debug'])

    # Link to all the other components
    application.register_blueprint(hello_blueprint, url_prefix='/hello')

    # Main route
    @application.route("/")
    def index():
        application.logger.debug('Running the main page. Application is running as a {} server.'.format(env))
        return render_template('index.html')

    return application


if __name__ == "__main__":
    # Get and start the flask application
    app = create_application()
    environment = os.getenv('ENVIRONMENT', 'production')

    # Configure host and port
    port = os.getenv('PORT', config[environment]['port'])
    host = os.getenv('HOST', config[environment]['host'])

    # Depending on the environment, run as a waitress server or a flask server
    if environment == 'production':
        from waitress import serve
        serve(app, host=host, port=port)
        app.logger.debug('Application is running at http://{}:{}'.format(host, port))
    else:
        app.run(host, port)
