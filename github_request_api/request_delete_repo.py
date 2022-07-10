import requests
import json

# path you want to request, and the repo name
path = "repos/philipesouzasantos/github-api-demo"

url = "https://api.github.com/{}"

# if the token is expired, you can generate another one here:
# https://github.com/settings/tokens
token = "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"

headers = {
    "authorization":
        f"Bearer {token}"
}

# delete request with header and data
# PS: you MUST have admin rights in your token to do that
response = requests.delete(url.format(path), headers=headers)
print(f'Saída:{response.text}')
