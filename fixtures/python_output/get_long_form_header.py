import requests

headers = {
    'Accept': 'application/json',
    'user-token': '75d7ce4350c7d6239347bf23d3a3e668',
}

response = requests.get('http://localhost:8080/api/retail/books/list', headers=headers)
