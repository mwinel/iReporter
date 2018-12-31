from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bycrypt = Bcrypt(app)

app.config['SECRET_KEY'] = "you-own-your-own"

# Register blueprints
from api.index import api as index_blueprint
app.register_blueprint(index_blueprint, url_prefix='/api/v1')

from api.auth import api as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth') 