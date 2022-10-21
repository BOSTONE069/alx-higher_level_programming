#!/bin/bash
#bash script for displaying length
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
