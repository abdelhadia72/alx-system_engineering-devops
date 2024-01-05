#!/bin/bash
# Get length of body of a request

url=$1
curl -sI "$url" | grep -i "Content-Length:" | awk '{print $2}'
