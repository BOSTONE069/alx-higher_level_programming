#!/bin/bash
#script that send request to a URL passed as an argument
curl -s -o /dev/dull -w %{http_code} $1
