#!/bin/bash

# A Bash script that:
    # takes in a URL,
    # sends a request to that URL
    # displays the size of the body of the response
# The size must be displayed in bytes
# Use `curl`
curl -s "${1}" | wc -c