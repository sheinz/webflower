#!/usr/bin/env python
#
# Just an example how to update an ip address
#
import httplib
import urllib
import sys

if len(sys.argv) != 2:
    print("Usage: {} [ip address]".format(sys.argv[0]))
    quit(1)

params = urllib.urlencode({'ip_address': sys.argv[1]})

headers = {"Content-Type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}

conn = httplib.HTTPConnection("54.229.82.159:80")
conn.request("POST", "/webflower/update_ip/", params, headers)
response = conn.getresponse()
print response.status, response.reason

data = response.read()
conn.close()
