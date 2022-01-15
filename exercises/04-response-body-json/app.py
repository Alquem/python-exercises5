import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)
response_dict = response.json()
#response_dict = {"hours":"19","minutes":"45","seconds":"06"}
print(response_dict)
print(f'Current time: {int(response_dict["hours"]):02d} hrs {int(response_dict["minutes"]):02d} min and {int(response_dict["seconds"]):02d} sec')