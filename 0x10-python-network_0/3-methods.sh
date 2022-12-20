#!/bin/bash
# This script prints all the methods available on a url
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
