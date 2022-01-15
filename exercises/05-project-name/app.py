import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)
response_dict = response.json()
print(response_dict["name"])