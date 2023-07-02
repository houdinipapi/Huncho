#!/bin/bash

# A Bash script that:
    # takes in a URL
    # displays all HTTP methods the server will accept.
# Use `curl`

curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-