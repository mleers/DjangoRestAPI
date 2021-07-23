FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r ./general_store/requirements.txt
RUN chmod +x /code/start.sh
RUN /code/start.sh
