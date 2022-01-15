import requests

def get_attachment_by_id(attachment_id):
    # your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    response_dict = response.json()
    
    for i in range(len(response_dict["posts"])):
        for j in response_dict["posts"][i]["attachments"]:
            if attachment_id == j["id"]:
                return j["title"]
        

print(get_attachment_by_id(137))