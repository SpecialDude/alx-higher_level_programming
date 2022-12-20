#!/bin/bash
# This script makes a request to the specifield url

curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
