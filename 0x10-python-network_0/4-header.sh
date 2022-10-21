#!/bin/bash
#script that takes in a URL as an argument, sends a GET request to the URL
curl -s "$1" -X GET -H "X-School-User-Id: 98"
