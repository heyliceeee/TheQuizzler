import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", parameters) # get request
response.raise_for_status() # raise an error if the status code is not 200

data = response.json() # get the data from the response

question_data = data["results"] # return the data