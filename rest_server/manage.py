#!/usr/bin/env python
import os
import sys
from sklearn.externals import joblib
from flask import jsonify, request
import traceback

# 모델 경로
file_directory = 'model'
file_name='%s/model.pkl' %file_directory

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_server.settings")
    try:
        forest = joblib.load(file_name)
        print('모델 있음!! model loaded')

    except Exception as e:
        print('모델 없음!! No model here - Train first')
        print(str(e))
        forest = None

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
