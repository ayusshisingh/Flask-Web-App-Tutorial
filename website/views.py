from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
	user = {'is_authenticated': True}  # Example user object
	return render_template("base.html", user=user)
