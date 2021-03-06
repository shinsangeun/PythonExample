from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from sklearn.externals import joblib
import traceback
import sys

app = Flask(__name__)
api = Api(app)

forest= None

# 모델 경로
model_file_name = './model.pkl'

forest = None

if model_file_name is None:
    print("모델 없음")
else:
    print("모델 있음")

# 웹서비스
@app.route('/predict/result', methods=['POST'])
def predict():
    if forest:
        try:
            param = request.json
            result = list(joblib.load(model_file_name).predict(param))
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('train first')
    return 'no model here'

if __name__ =='__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 8080

    try:
        forest = joblib.load(model_file_name)
        print('model loaded')

    except Exception as e:
        print('No model here - Train first')
        print(str(e))
        clf = None
    app.run(host='0.0.0.0', port=port, debug=True)