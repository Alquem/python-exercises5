import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")
response_dict = {404:"The URL you asked is not found",
                503:"Unavailable right now",
                200:"Everything went perfect",
                400:"Something is wrong on the request params"
                }
if response.status_code in response_dict.keys():
    print(response_dict[response.status_code])
else:
    print(response.status_code)