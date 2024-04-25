FROM python:3.10.12

RUN mkdir /development

WORKDIR /development

ADD . /development/

RUN python -m pip install --upgrade pip

RUN pip install -r /development/requirements.txt
