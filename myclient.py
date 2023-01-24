import requests

url = f"http://localhost:8000?choice={choice}&amount={amount}"

choice=input(type=int)
amount=input(type=int)

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)