import json
import requests

# path you want to request
path = "repos/philipesouzasantos/github_api_demo/contents/{}"

# name of the  files
name_file = [
    ('copy1', ('hello.txt', open('hello.txt', 'rb'), 'txt')),
    ('copy2', ('hello2.txt', open('hello2.txt', 'rb'), 'txt'))
]

# github api url
url = "https://api.github.com/{}"

print(url.format(path))

# you can generate a token here:
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

for name in name_file:
    print(name[1][0])

# post request with header and data
    response = requests.put(url.format(path.format(name[1][0])), headers=headers, json=data)

# load json
output = json.loads(response.text)
print(output)