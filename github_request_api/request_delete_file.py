import requests
import json

# path you want to request, and the repo name
path = "repos/philipesouzasantos/github_api_demo/contents/{}"

url = "https://api.github.com/{}"

# type the name of the files you want to delete
name_file = [
    ('copy1', ('hello.txt', open('hello.txt', 'rb'), 'txt')),
    ('copy2', ('hello2.txt', open('hello2.txt', 'rb'), 'txt'))
]

# if the token is expired, you can generate another one here:
# https://github.com/settings/tokens
token = "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"

headers = {
    "authorization":
        f"Bearer {token}",

}
# insert parameters here
data = {
    # reference: https://docs.github.com/pt/rest/reference/issues
    "sha": "e75154b7c390fdc4aa85d86e0a191be255a00627",
    "message": "commit message"
}

for name in name_file:
    print(name[1][0])
    # delete request with header and data
    # PS: you MUST have admin rights in your token to do that

    response = requests.delete(url.format(path.format(name[1][0])), headers=headers, json=data)
    print(response)

print(f'Saída:{response.text}')
