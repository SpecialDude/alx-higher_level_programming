#!/bin/bash
# This script send a request to the specified url and prints the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
