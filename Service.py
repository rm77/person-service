from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
import os

'''
flask -> pip install flask
flask_restful -> pip install flask_restful
run server dengan python Service.py
'''

#gunakan model Persons_Model 
from Persons_Model import *

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


api.add_resource(Version,'/version')
api.add_resource(PersonList,'/personlist')
api.add_resource(Person,'/person/<id>')
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)


		


