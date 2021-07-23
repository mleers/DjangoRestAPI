FROM python:3.7-alpine3.12
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r ./general_store/requirements.txt
