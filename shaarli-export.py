#!/usr/bin/python
import time
import jwt
import requests
import json

# user configuration
SHAARLI_SERVER_URL = "https://<your.url.here>"
SHAARLI_API_SECRET = "<your.secret.here>"

# static configuration
SHAARLI_HASH_ALGORITHM = "HS512"

if __name__ == "__main__":
  now = int(time.time())
  payload = { "iat" : now }
  token = jwt.encode(payload, SHAARLI_API_SECRET, algorithm = SHAARLI_HASH_ALGORITHM)

  url = SHAARLI_SERVER_URL + "/api/v1/links"
  params = { "limit" : "all" } # get all links without pagination
  headers = { "Authorization" : "Bearer " + token }

  r = requests.get(url, params = params, headers = headers)
  print json.dumps(r.json(), indent = 4, sort_keys = True)
