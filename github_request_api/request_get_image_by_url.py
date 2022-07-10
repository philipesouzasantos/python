import requests

url = "https://avatars.githubusercontent.com/u/36214668?v=4"

# get method pointing to the image
response = requests.get(url)

# open a new file with the name specified
fp = open("my_profile.png", "wb")

# write the content on file
fp.write(response.content)

# close the file after you finish it
fp.close()