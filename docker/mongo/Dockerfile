FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME root
ENV MONGO_INITDB_ROOT_PASSWORD password
ENV MONGO_INITDB_DATABASE: pysharedb

ADD ./script/mongo-init.js /docker-entrypoint-initdb.d
