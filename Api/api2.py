import sys
import os
import shutil
import time
import traceback

from flask import Flask, request, jsonify
from urllib.request import urlopen
import urllib.request
from sklearn.externals import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

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

# 구동 메인
if __name__ == '__main__':
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