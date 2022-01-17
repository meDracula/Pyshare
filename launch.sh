#!/bin/sh
echo "======= Initilazing ======="
export PYTHONPATH="${PYTHONPATH}:${PWD}/app"

echo "======= Requirements ======="
echo "Do you need to check requirements? [y/n]: "
read var
if [ $var = "y" ]; then
	pip install -r requirements.txt
fi

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
flask run

echo "exit 0"
