FROM python:3.10-bullseye

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip

# Install requirements
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
