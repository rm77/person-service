from flask import Flask
from flask_restful import Resource, Api

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


api.add_resource(PersonList,'/personlist')
api.add_resource(Person,'/person/<id>')
if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)


		


