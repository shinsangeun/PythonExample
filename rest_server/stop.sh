#!/bin/bash

kill -9 `ps auxw | grep runserver | awk '{print $2}'`
echo "=== Stop django server ...: $2 ==="
