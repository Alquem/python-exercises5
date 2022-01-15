import requests

def get_post_tags(post_id):
    # your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    response_dict = response.json()
    
    for i in range(len(response_dict["posts"])):
        if response_dict["posts"][i]["id"] == post_id:
            return response_dict["posts"][i]["tags"]
    


print(get_post_tags(146))