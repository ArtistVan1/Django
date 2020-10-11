import  requests,pprint

payload = {
    'username': 'jj',
    'password': '12345678'
}

response = requests.post('http://localhost/api/mgr/signin',
              data=payload)

pprint.pprint(response.json())

payload1 = {
    'action':'list_customer'
}

response1 = requests.get('http://localhost/api/mgr/customers',params=payload1)

pprint.pprint(response1.json())
