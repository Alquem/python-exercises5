import requests

def get_titles():
    # your code here
    titles = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    response_dict = response.json()
    for i in range(len(response_dict["posts"])):
        titles.append(response_dict["posts"][i]["title"])
    return titles


print(get_titles())