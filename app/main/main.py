from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='static',template_folder='templates', static_url_path='/main/static')
# , static_url_path='/app.main.static'

@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')

@main.route('/profile', methods = ['POST', 'GET'])
def profile():
    return render_template('profile.html')