from django.shortcuts import render
from sensor.forms import *
from sklearn.externals import joblib
from flask import jsonify, request
import traceback
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import *
from rest_framework import viewsets

def post(request):
    print("POST 실행", request)
    if request.method == "POST":
        form = SensorSerializer(data=request.data)
        #form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            print("POST 성공")
            return HttpResponse("POST Method",form.data)
    else:
        # form = PostForm()
        print("POST 실패")
        return HttpResponse("Your response")



# 모델 경로
file_directory = 'model'
file_name='%s/model.pkl' %file_directory

forest = None

# 웹서비스
def predict(request):
    print("predict 실행", request)
    if request.method == "POST":
        print("POST 성공")
        if forest:
            print("forest 있음")
            try:
                param = request.json
                print("param=>", param)
                result = list(joblib.load(file_name).predict(param))
                print("result=>", result)
                return HttpResponse(result)
              #  return jsonify({'result': result})
            except Exception as e:
                return jsonify({'error': str(e), 'trace': traceback.format_exc()})
        else:
            print('train first')
        return 'no model here'
    else:
        print("POST 실패")
        return ("Not Post Method")

class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
