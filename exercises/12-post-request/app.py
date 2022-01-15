import requests

# your code here
url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)