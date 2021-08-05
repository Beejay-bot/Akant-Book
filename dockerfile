FROM python:3.8-slim-buster
# This ensures that our python output like print() or error logs is sent straight to the terminal
ENV PYTHONBUFFERED=1
WORKDIR / django
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt
