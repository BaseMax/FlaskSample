from flask import Flask
from flask import Response
from flask import render_template
from flask import Blueprint
# from flask import request
from flask import request, jsonify
import uuid
import json
# from app import app, mongo
from pymongo import MongoClient
from bson import json_util
from flask import redirect

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'DB'
COLLECTION_LINK="Service"

class flaskLocal(Flask):
	def process_response(self, response):
		return(response)

app = flaskLocal(__name__)

#app.config.SERVER_NAME = 'asrez.base:80'
#app.config

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/single')
def single():
	return render_template('single.html')

@app.route('/projects/')
def projects():
	return 'The project(s) page'

@app.route('/about')
def about():
	return 'The about page'
# doc_count = col.count_documents(filter, skip=skip)
# results = col.find(filter).sort(sort).skip(skip).limit(limit)

@app.route('/service/', methods=['GET','POST'], defaults={'value':None})
@app.route('/service/<string:value>/',methods=['GET'])
def service(value):
	mainSite="http://test.base/"
	site="http://test.base/service/"
	if value == None or value == '':
		if request.method == "GET":
			return render_template('index.html', method=request.method, random=uuid.uuid4().hex.upper()[0:7].lower(), site=site, mainSite=mainSite)
		else:
			return render_template('post.html', message="Has been submit...", method=request.method, value=value, status="post", site=site, mainSite=mainSite)
	elif value == "api":
		return render_template('api.html', site=site, mainSite=mainSite)
	else:
		return "Error!"

if __name__ == '__main__':
	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	collectionLink = connection[DB_NAME][COLLECTION_LINK]
	# app.run(host='test.base', port=80, debug=False)
	app.run(port=80)
