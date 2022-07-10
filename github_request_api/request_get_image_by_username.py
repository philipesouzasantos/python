import json
import requests

# github username
git_username = "philipesouzasantos"
url = f"https://api.github.com/users/{git_username}"

# get to url profile
response = requests.get(url)

# load json
output = json.loads(response.content)

# get image url from json
response_img = requests.get(output['avatar_url'])

fb = open("my_profile_2.png", "wb")
fb.write(response_img.content)
fb.close()

