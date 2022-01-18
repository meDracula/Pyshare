#!/bin/sh
echo "======= Initilazing ======="
export PYTHONPATH="${PYTHONPATH}:${PWD}/app"

if [ $1 = "req" ]; then
	echo "======= Requirements ======="
	pip install -r requirements.txt
fi
shift

echo "======= Launching Docker ======="
function dockerUp () {
	cd docker
	docker-compose up --build -d
	cd ..
}

docker inspect --format="{{.State.Running}}" PyshareMongo
if [ $? -eq 0 ]; then
	echo "container is already up"
else
	echo "container is down"
	echo "initizalating start up procedure for docker..."
	dockerUp
fi

echo "======= Launching Flask ======="
if [ $1 = "key" ]; then
	python utils/gen_secret_key.py
fi

flask run

echo "exit 0"
