#!/bin/bash
#script that takes in a URL, sends a POST request to the passed URL
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" $1
