import requests
import json
import webbrowser
import os


# Function to get animal information
def get_animal_info(animal_name, api_key):
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        'X-Api-Key': api_key
    }

    try:
        response = requests.get(url, headers=headers, params={'name': animal_name})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print("HTTP request successful.")
        return response.json()  # Return the JSON response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    return None


# Function to generate an HTML file with animal information
def generate_html(animal_data, animal_name):
    if not animal_data:
        print("No data provided to generate HTML.")
        return False

    html_content = f"""
    <!DOCTYPE html>
    <html lang="bg">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Information about {animal_name.capitalize()}</title>
    </head>
    <body>
        <h1>Information about {animal_name.capitalize()}</h1>
        <ul>
    """

    for animal in animal_data:
        html_content += f"""
        <li>
            <h2>{animal.get('name', 'Unknown')}</h2>
            <p><strong>Scientific Name:</strong> {animal.get('scientific_name', 'Unknown')}</p>
            <p><strong>Habitat:</strong> {animal.get('habitat', 'Unknown')}</p>
            <p><strong>Diet:</strong> {animal.get('diet', 'Unknown')}</p>
            <p><strong>Location:</strong> {animal.get('locations', 'Unknown')}</p>
            <p><strong>Characteristics:</strong> {animal.get('characteristics', 'Unknown')}</p>
        </li>
        """

    html_content += """
        </ul>
    </body>
    </html>
    """

    try:
        with open("animals.html", "w", encoding='utf-8') as file:
            file.write(html_content)
        print("HTML file content written successfully.")
        print("Website was successfully generated to the file animals.html.")
        return True
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        return False


# Main function
def main():
    api_key = 'nAjjhYhpOUbxkLUor9zMzA==oSEFYYNNUdbxXqyy'  # Replace with your actual API key
    animal_name = input("Enter a name of an animal: ")

    # Fetch animal information
    animal_data = get_animal_info(animal_name, api_key)

    if animal_data:
        # Print fetched data for debugging
        print("Fetched animal data:")
        print(json.dumps(animal_data, indent=4))
        # Generate HTML file with animal information
        if generate_html(animal_data, animal_name):
            # Open the generated HTML file in the default web browser
            webbrowser.open("file://" + os.path.realpath("animals.html"))
    else:
        print("No information found for the specified animal.")


if __name__ == "__main__":
    main()
