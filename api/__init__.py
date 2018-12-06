from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'you-own-your-own'
jwt = JWTManager(app)

# Register blueprints
from api.index import api as index_blueprint
app.register_blueprint(index_blueprint, url_prefix='/api/v1')

from api.auth import api as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth') 