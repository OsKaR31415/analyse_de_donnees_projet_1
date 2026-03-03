#!/usr/bin/python3
from os import system

system("jupyter nbconvert --to python --no-prompt report.ipynb")
