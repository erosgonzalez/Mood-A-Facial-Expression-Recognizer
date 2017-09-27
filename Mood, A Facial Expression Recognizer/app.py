#Flask website. It incorporates html and python. 
from flask import Flask, render_template, request, url_for, redirect
from string import Template
import requests
import os
from API import user

HTML_TEMPLATE =Template

app = Flask(__name__)

@app.route('/') #homepage
def home():
	return render_template("homepage.html")

@app.route('/results', methods = ['GET', 'POST'])
def results():#video result
	return render_template("videoEmotion.html")

def userEmotion(): #will serve for jinja inside of videoEmotion.html
	ID = user()
	return ID

app.jinja_env.globals.update(userEmotion=userEmotion)


if __name__ == '__main__':

	app.run(debug=True, use_reloader=True, port=int(os.getenv('PORT', 8080)), host = os.getenv('IP', '0.0.0.0'))
