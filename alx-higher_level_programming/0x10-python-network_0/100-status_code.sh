# A Bash script that:
    # sends a request to a URL passed as an argument,
    # displays only the status code of the response
# Do not use any pipe, redirection, etc.
# Do not use `;` and `&&`
# Use `curl`
curl -s -o /dev/null -w "%{http_code}" "$1"