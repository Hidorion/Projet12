import requests
import json
from pprint import pprint

API_KEY = "2a105mNgp56RlYJ5jj7fpgDDKu"  # Your API_KEY here
api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"

image_path_1 = "images/ressources/image_objet/banane.png"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = "images/ressources/image_objet/bananes.jpg"
image_data_2 = open(image_path_2, 'rb')

data = {
    'organs': ['fruit', 'fruit']
}

files = [
    ('images', (image_path_1, image_data_1)),
    ('images', (image_path_2, image_data_2))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)


pprint(response.status_code)
pprint(json_result['results']['species']['commonNames'])