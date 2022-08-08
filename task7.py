import os
import sys
import json
import requests
from flask import Flask, render_template 


app = Flask(__name__,template_folder='./templates',static_folder='./static')
@app.route('/')
def displayJobDetails():
    # Write a code to give call to json file and then render html page
	url = 'https://raw.githubusercontent.com/Yingkai-Ma/ITSC_3155_080_Sprint2-BS-Task1and2/main/pythonBeautifulSoup--master/jobDetails.json'
	response = requests.get(url)
	responseJSON = response.json()
	return render_template('index.html', responseJSON=responseJSON)