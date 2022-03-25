#import Flask
from flask import Flask

#create registerd app as a blueprint
def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = '\x8d-\x83\x1bD\xa6\xb7wt\xa3\xc3\xef\xbd\xd8\x90\xb5\x8cJ\xba\x04\xd7,\xf8S'

    #import the app
    from . import choiceurl
    app.register_blueprint(choiceurl.bp)

    return app
