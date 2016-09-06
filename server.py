# python libs
from flask import Flask, render_template, request, redirect, json
import requests

# 3rd party libs
from boxsdk import OAuth2
from boxsdk import Client

# my libs
from teacher import Teacher


# boxsdk OAuth2 setup
oauth = OAuth2(
	client_id='YOUR CLIENT_ID',
	client_secret='YOUR CLIENT_SECRET'
	# TODO: STORE THE TOKENS
	# store_tokens='HvlozVj2c5zYT2DmOlYK82IqdWPZSzrf'
)

auth_url, csrf_token = oauth.get_authorization_url('http://localhost:5000/callback')

# set up authorize client to use API
client = Client(oauth)


app = Flask("__name__")


@app.route('/')
def index():
	""" Homepage """

	# For now, when users hit our homepage, they 
	# are automatically requested to give app access
	# to their box account. If authorized, our
	# app redirects them to a generic profile page

	# boxsdk OAuth2 setup

	return redirect(auth_url)


@app.route('/login')
def login():
	""" User login """

	# authenticate and create Teacher instance

	pass


@app.route('/logout')
def logout():
	""" Use logout """

	pass


@app.route('/callback')
def callback():
	""" Get authorization code and access tokens """

	# Involves getting credentials from Box
	state = request.args.get('state')
	code = request.args.get('code')

	assert state == csrf_token
	access_token, refresh_token = oauth.authenticate(code)

	return redirect('/profile')


@app.route('/profile')
def profile():
	""" A Generic Profile Page """

	# get the current user Box username
	me = client.user(user_id='me').get()

	return render_template('profile.html', me=me)


@app.route('/folders')
def folders():
	""" Generic route to show Box users root directory and sub directories """

	# Box root directory and all items in it,
	# which includes subdirectories
	root_folder = client.folder(folder_id='0').get()
	items = client.folder(folder_id='0').get_items(limit=100, offset=0)

	return render_template('folders.html', root_folder=root_folder, items=items)



if __name__ == "__main__":
	app.run(debug=True)
