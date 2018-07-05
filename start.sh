#!/bin/bash
docker build -t proxy .
docker run -d --restart always -p 172.17.0.1:8000:8000 --name proxy --env-file env.in proxy
echo "don't forget to delete you env.in"
