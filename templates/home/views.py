from flask import render_template, Blueprint
half_blueprint = Blueprint('halfnhalf',__name__)

@half_blueprint.route('/')
@half_blueprint.route('/halfnhalf')
def index():
	return render_template("index.html")
