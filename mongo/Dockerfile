FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME root
ENV MONGO_INITDB_ROOT_PASSWORD password
ENV MONGO_INITDB_DATABASE pysharedb

ENV BROWSERSLIST_IGNORE_OLD_DATA=1

ADD ./mongo/mongo-init.js /docker-entrypoint-initdb.d
