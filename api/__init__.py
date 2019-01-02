from flask import Flask
from flask_jwt_extended import JWTManager
from api.errors.request_errors import RequestError

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "you-own-your-own"

# Request exceptions
app.errorhandler(404)(RequestError.not_found)
app.errorhandler(405)(RequestError.method_not_allowed)

# Register blueprints
from api.index import api as index_blueprint
app.register_blueprint(index_blueprint, url_prefix='/api/v1')

from api.auth import api as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth')

from api.redflags import api as redflags_blueprint
app.register_blueprint(redflags_blueprint, url_prefix='/api/v1')