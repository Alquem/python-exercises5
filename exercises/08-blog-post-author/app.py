import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)
response_dict = response.json()
print(response_dict["posts"][0]["author"]["name"])