from django.shortcuts import render
from sensor.forms import *
from sklearn.externals import joblib
from flask import jsonify, request
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import *
import simplejson as json

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