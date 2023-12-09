import requests

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
data = response.json()
result_data = data["results"]

question_data = result_data
