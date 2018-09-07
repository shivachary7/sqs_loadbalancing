FROM python:3
## python 3 image
WORKDIR /usr/src/app
## setting working directory to usr/src/app
COPY WorkerPythonScript.py  ./
## copying the worker file
