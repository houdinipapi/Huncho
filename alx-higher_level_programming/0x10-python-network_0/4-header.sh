#!/bin/bash

# A Bash script that:
    # takes in a URL as an argument,
    # sends a GET request to the URL,
    # displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98.
# Use curl

curl "$1" -sH "X-School-Use-Id: 98"