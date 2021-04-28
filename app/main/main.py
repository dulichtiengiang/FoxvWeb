from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='static',template_folder='templates/main')

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/profile', methods = ['POST', 'GET'])
def profile():
    return render_template('profile.html')