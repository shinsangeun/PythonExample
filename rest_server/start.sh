#!/bin/sh

echo "=== Start django server ...  ==="
python3 manage.py runserver 0.0.0.0:8000 &

