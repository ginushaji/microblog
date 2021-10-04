from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user={'username':'Hari Inamadugu'}
	posts=[
	{
	'author':{'username':'vasudha'},
	'body':'I am learning AWS'},
	{
	'author':{'username':'bhaskar'},
	'body':'I already know AWS'
	}
	]
	return render_template('index.html', title= 'Home', user=user, posts= posts)
