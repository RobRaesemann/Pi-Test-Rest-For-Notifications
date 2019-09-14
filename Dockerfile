FROM python:3.7
ADD . /workorder
WORKDIR /workorder
RUN pip install -r requirements.txt