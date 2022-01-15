import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"
myobj = {"Content-Type":"application/json"}
json_obj = {
    "id":2323,
    "title": "Very big project"
}

resp = requests.post(url, headers=myobj, json=json_obj)


print(resp.text)