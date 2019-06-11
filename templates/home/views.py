from flask import render_template, Blueprint
home_blueprint = Blueprint('home',__name__)

@home_blueprint.route('/')
@home_blueprint.route('/home')
def index():
	return render_template("index.html")


@home_blueprint.route('/visualization_i2i')
def visualization_i2i():
    return render_template('visualization_i2i.html')

@home_blueprint.route('/visualization_i2l')
def visualization_i2l():
    return render_template('visualization_i2l.html')

@home_blueprint.route('/visualization_l2i')
def visualization_l2i():
    return render_template('visualization_l2i.html')

@home_blueprint.route('/dataset')
def dataset():
    return render_template('dataset.html')

@home_blueprint.route('/people')
def people():
    return render_template('people.html')
