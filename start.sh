#!/bin/bash
sudo docker build -t proxy .
sudo docker run -d --restart always  -p 127.0.0.1:8000:8000 --name proxy --env-file env.in proxy python /root/forward.py
echo '
BASIC_USERNAME=
BASIC_PASS=
DEST_URL=
' > env.in
