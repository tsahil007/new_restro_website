from flask import Blueprint, render_template
views = Blueprint('views', __name__)

@views.route('/')
def home_get():
    return render_template('index.html')