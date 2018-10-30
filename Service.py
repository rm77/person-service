from flask import Flask
from flask_restful import Resource, Api

from Persons_Model import *
from Users_Model import *

p_model = Persons_Model()

app = Flask(__name__)
api = Api(app)

class PersonList(Resource):
	def get(self,id=''):
		return p_model.list()
	def post(self):
		args = parser.parse_args()
		data = args['data']
		return p_model.add(data)

class Person(Resource):
	def get(self,id):
		return p_model.get(id)
	def delete(self,id):
		return p_model.remove(id)

class Auth(Resource):
	def post(self):
		


api.add_resource(PersonList,'/personlist')
api.add_resource(Person,'/person/<id>')
if __name__ == '__main__':
	app.run(debug=True)


		


