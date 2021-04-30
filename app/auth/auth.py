from flask import Blueprint, render_template
from app.auth.form import LoginForm

auth = Blueprint('auth', __name__, static_folder='static',template_folder='templates', static_url_path='/auth/static')
# , static_url_path='/app.main.static'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form = form)