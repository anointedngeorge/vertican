#!/bin/bash

port_number=8023
app_name=vertican
lsof -i :$port_number && kill $(lsof -t -i:$port_number)
gunicorn -w 3 $app_name.wsgi:application -b 0.0.0.0:$port_number 