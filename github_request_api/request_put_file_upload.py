import json
import requests

# path you want to request
path = "repos/philipesouzasantos/github_api_demo/contents/{}"
# file name to upload
name_file = "hello3.txt"

# github username
url = "https://api.github.com/{}"

print(url.format(path))

# if the token is expired, you can generate another one here:
# https://github.com/settings/tokens
token = "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"

headers = {
    "authorization":
        f"Bearer {token}"
}

# insert parameters here
data = {
    # reference: https://docs.github.com/pt/rest/reference/issues
    "message": "my commit message",
    # base64 reference: https://www.base64encode.org/
    "content": "cHJpbnQoImhlbGxvIHdvcmxkIik="
}

# post request with header and data
response = requests.put(url.format(path.format(name_file)), headers=headers, json=data)

# load json
output = json.loads(response.text)
print(output)