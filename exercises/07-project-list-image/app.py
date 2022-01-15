import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
response_dict = response.json()
print(response_dict[-1]["images"][-1])