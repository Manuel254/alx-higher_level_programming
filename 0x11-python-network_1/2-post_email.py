#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__ == '__main__':
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    email = {'email': argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(f"Your email is: {response.read()}")

