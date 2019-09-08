from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=int)
        parser.add_argument('result',type=str)
        args = parser.parse_args()

        value = args['value']
        result = args['result']

        if result is not None :
            return {'Message': "Success", 'code': 0, "Result": result}
        else:
            return {'Message': "error", 'code': 500}

api.add_resource(RegistUser, '/ai/result')


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)