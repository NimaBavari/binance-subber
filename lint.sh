#!/bin/bash
isort -rc main.py
autoflake -r --in-place --remove-unused-variables main.py
black -l 120 main.py
flake8 --max-line-length 120 main.py