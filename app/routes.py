from flask import Blueprint, template_rendered, url_for
from flask import current_app
from flask.templating import render_template
from . import db

main_bp = Blueprint('main_bp', __name__, static_folder='static')

@main_bp.route('/', methods = ['POST', 'GET'])
def index():
    # print(app.config)
    print(current_app.config)
    return render_template('index.html')

@main_bp.route('/profile', methods = ['POST', 'GET'])
def profile():
    return render_template('profile.html')

@main_bp.route('/home', methods = ['POST', 'GET'])
def home():
    return render_template('profile.html')