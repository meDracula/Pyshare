FROM python:3.9 AS complier

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN python -m pip install --upgrade pip

COPY ./flask/requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.9 AS build

COPY --from=complier /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /flask
COPY ./flask .

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

RUN chmod +x docker-entrypoint-flask.sh

ENTRYPOINT ["./docker-entrypoint-flask.sh"]
