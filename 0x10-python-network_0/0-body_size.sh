#!/bin/bash
# This script takes in a url and sends a request to that url
# and displays the size of the body of the response
curl -s -w %size_upload $1
