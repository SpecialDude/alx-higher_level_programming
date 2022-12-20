#!/bin/bash
# This script sends a json POST request to the specified url
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
