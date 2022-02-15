import requests

req = requests.post('https://jsonplaceholder.typicode.com/posts', data = {'title': 'title', 'body': 'example body', 'userId': 1 } )

print(req.text)
