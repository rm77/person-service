from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import os
from Persons_Model import *
from Auth_Model import *

p_model = Persons_Model()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('data')

class PersonList(Resource):
	def get(self,id=''):
		return p_model.list()
	def post(self):
		args = parser.parse_args()
		data = json.loads(args['data'])
		return p_model.add(data)

class Person(Resource):
	def get(self,id):
		return p_model.get(id)
	def delete(self,id):
		return p_model.remove(id)

class Version(Resource):
	def get(self):
		iplist = os.popen("ifconfig eth0 | grep 'inet addr'").readlines()
		my_ip = "".join(iplist)
		return { 'info' : '0.01', 'ip' : "{}" . format(my_ip)  }

class Auth(Resource):
	def post(self):
		args = parser.parse_args()
		data = json.loads(args['data'])
		username = data['username']
		password = data['password']
		auth_model = Auth_Model()
		auth_result = auth_model.login(username,password)
		return {'status' : 'OK'}
		#print auth_result
		#if (auth_result is not None):
	#		return { 'status' : 'OK' }
	#	else:
#			return { 'status': 'ERROR' }
	def get(self,token=''):
		if (token==''):
			return { 'status' : 'OK' }
		auth_model = Auth_Model()
		auth_result = auth_model.cek_token(token)
		if (auth_result is not None):
			return {'status' : 'OK'}
		else:
			return { 'status' : 'ERROR' }

api.add_resource(Version,'/version')
api.add_resource(PersonList,'/personlist')
api.add_resource(Person,'/person/<id>')

api.add_resource(Auth,'/auth')

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)


		


