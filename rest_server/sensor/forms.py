from django.forms import ModelForm
from sensor.models import *
from sklearn.externals import joblib
from flask import jsonify, request
import traceback

class Form(ModelForm):
    class Meta:
        model=Sensor
        fields=['x','y','z']


