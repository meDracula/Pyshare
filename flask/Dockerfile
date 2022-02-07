FROM python:3.9

WORKDIR /flask
COPY ./flask .

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

RUN python -m pip install --upgrade pip && \
	pip install -r requirements.txt

RUN chmod +x docker-entrypoint-flask.sh

ENTRYPOINT ["./docker-entrypoint-flask.sh"]

