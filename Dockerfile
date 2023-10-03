FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3.10 python3-pip

RUN pip3 install --upgrade pip

RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
