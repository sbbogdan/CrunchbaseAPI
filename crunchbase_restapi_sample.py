# Crunchbase REST API quickstart sample

# imports
import os.path, requests, json, pprint

# UUID of a company to search for
uuid = '<uuid_goes_here>'

# Your crunchbase API key
cb_key = '<crunchbase_api_key_goes_here>'

# The URI for the batch query Rest API call
request_url = 'http://api.crunchbase.com/v3.1/batch'

# The required HttpRequest headers; the crunchbase API key is parameterized with header 'X-Cb-User-Key'
headers = {'Content-type': 'application/json', 'X-Cb-User-Key' : cb_key}

# Build your request, parameterize the company UUID; request investors, funding_rounds
data = {"requests": [ { "type": "Organization", "uuid": uuid, "relationships": ["investors", "funding_rounds"]} ] }
payload = json.dumps(data)

# Issue Crunchbase REST API call, print the response
ret = requests.post(request_url, headers=headers, data=payload)
pprint.pprint(ret.json())