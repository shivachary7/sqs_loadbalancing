FROM PytthonImage #This image has python installed

# copying worker python file to Docker Working directory
ADD WorkerPythonScript.py /usr/local/bin/WorkerPythonScript.py

# running worker python file on Docker startup
ENTRYPOINT ["./usr/local/bin/WorkerPythonScript.py"]
