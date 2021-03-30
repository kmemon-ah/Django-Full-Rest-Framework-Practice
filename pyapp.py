import requests
import json

URL = 'http://127.0.0.1:8000/csrud/25'

# Read
def get_data( id = None):
    data = {}
    if id is not None:
        data = {'id' : id}

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.get(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

get_data()

# Create
def post_data():
    data = {
    'name':'Emon',
    'roll': 199,
    'city':'Dhak'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
    'name':'emona'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.patch(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
    'id':17,
    }

    headers = {'content-Type':'application/json'}


    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# delete_data()