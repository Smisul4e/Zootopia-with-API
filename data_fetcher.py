import requests
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('nAjjhYhpOUbxkLUor9zMzA==oSEFYYNNUdbxXqyy')

def fetch_data(animal_name):

    """
    Fetch animal data from the API.
    """

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
      return response.json()
    else:
      return []