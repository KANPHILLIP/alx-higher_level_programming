#!/bin/bash
# This script sends the a request to rhe url and displays the size of the response body in bytes
curl -s "$1" | wc -c
