from django.shortcuts import render
from sensor.forms import *
from sklearn.externals import joblib
from flask import jsonify, request
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import *
import simplejson as json
import numpy as np

# 모델 경로
file_directory = 'model'
file_name='%s/model.pkl' %file_directory

forest = None

try:
    forest = joblib.load(file_name)
    print('model loaded')

except Exception as e:
    print('No model here - Train first')
    print(str(e))
    forest = None

# 웹서비스
@csrf_exempt
def predict(request):
    body_code = request.body.decode('utf-8')
    body=json.loads(body_code)
    if request.method == "POST":
        print("POST success")
        if forest:
            try:
                param = body
                print("param=>", param)
                result = list(joblib.load(file_name).predict(param))
                print("result=>", result)
                return JsonResponse({'result': result})
            except Exception as e:
                return jsonify({'error': str(e), 'trace': traceback.format_exc()})
        else:
            print('train first')
        return 'no model here'
    else:
        print("POST error")
        return ("Not Post Method")

# 웹서비스
@csrf_exempt
def acceler(request):
    body_code = request.body.decode('utf-8')
    body = json.loads(body_code)
    if request.method == "POST":
        if forest:
            try:
                i = 0
                result2 = []
                while i < len(body):
                    result_list = list(body[i].values())
                    i += 1
                    array_list = np.array(result_list).reshape(-1, 3)

                    k = 0
                    while k < len(array_list):
                        result = list(joblib.load(file_name).predict(array_list))[k]
                        k += 1

                    result2.append(result)

                return JsonResponse({'result': result2})
            except Exception as e:
                return JsonResponse({'error': str(e), 'trace': traceback.format_exc()})
        else:
            print('train first')
        return 'no model here'
    else:
        print("POST error")
        return ("Not Post Method")