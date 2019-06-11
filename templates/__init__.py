from templates.home.views import half_blueprint
from flask import Flask
app = Flask(__name__,
            static_folder='./public',
            template_folder="./static/templates")
# register the blueprints
app.register_blueprint(half_blueprint)
