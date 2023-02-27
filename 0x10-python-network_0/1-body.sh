#!/bin/bash
# This script makes a request to a specified url and prints the response body
curl -sX GET "$1" -L
