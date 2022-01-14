#!/bin/sh
echo "======= Initilazing ======="
export PYTHONPATH="${PYTHONPATH}:${PWD}/app"

echo "======= Requirements ======="
pip install -r requirements.txt

echo "======= Launching Docker ======="
#cd docker/
#docker-compose up --build -d
#cd ..

echo "======= Launching ======="
flask run

echo "exit 0"
