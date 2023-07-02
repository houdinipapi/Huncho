#!/bin/bash

# A Bash script that:
    # sends a JSON POST request to a URL passed as the first argument,
    # displays the body of the response
# The script must send a `POST` request with the contents of a file,
# passed with the filename as the second argument of the script, in the body of the request.
# Use `curl`

curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"