#!/bin/bash

CONTAINER="pyshare_mongo"

function backup() {
	docker exec -it $CONTAINER mongodump --verbose --db pysharedb --out /vol/ -u $1 -p $2
}

function restore() {
	docker exec -it $CONTAINER mongorestore --verbose --db pysharedb /vol/pysharedb/ -u $1 -p $2
}

if [ $(docker inspect --format="{{.State.Running}}" $CONTAINER) == "false" ]; then
	echo "container pyshare_mongo is not running"
	exit 1
fi

read -p "Do you want to restore or backup [r/b] " action
read -p "Enter your mongodb username: " user
read -p "password: " password

case $action in
	"b") backup $user $password;;
	"r") restore $user $password;;
	*) echo "You have to enter r or b!";;
esac

unset password
exit 0
