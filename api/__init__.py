from flask import Flask

app = Flask(__name__)

# Register blueprints
from api.index import api as index_blueprint
app.register_blueprint(index_blueprint, url_prefix='/api/v1')

from api.auth import api as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth') 