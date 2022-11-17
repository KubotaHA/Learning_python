#!/bin/bash

echo
echo "# coverage run -m unittest test_python_learning.py"
coverage run -m unittest test_python_learning.py

echo
echo "# coverage report"
coverage report

echo
echo "# coverage html"
coverage html
echo
