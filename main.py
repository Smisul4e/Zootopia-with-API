import requests


def get_animal_info(animal_name, api_key):
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        'X-Api-Key': api_key
    }

    try:
        response = requests.get(url, headers=headers, params={'name': animal_name})
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        return f"Error occurred: {err}"


def process_response(response):
    if isinstance(response, requests.Response):
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: {response.status_code}, {response.json().get('error', 'Unknown error')}")
    else:
        print(response)


def get_user_input():
    return input("Enter the name of the animal: ")


def main():
    api_key = 'nAjjhYhpOUbxkLUor9zMzA==oSEFYYNNUdbxXqyy'
    animal_name = get_user_input()
    response = get_animal_info(animal_name, api_key)
    process_response(response)


if __name__ == "__main__":
    main()
