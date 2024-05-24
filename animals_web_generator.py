from dotenv import load_dotenv
load_dotenv()
import data_fetcher


def serialize_animal(animal_obj):
    """
    Serialize an animal object into HTML format for a card.
    """
    content = ''
    if 'locations' in animal_obj and animal_obj['locations']:
        location = animal_obj['locations'][0]
    else:
        location = "undefined"

    content += "<li class=\"cards__item\">"
    content += "<div class=\"card__title\">"
    content += f"{animal_obj['name']}</div>"
    content += "<p class=\"card__text\">"
    content += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>"
    content += f"<strong>Location:</strong> {location}<br/>"

    if 'type' in animal_obj['characteristics']:
        animal_type = animal_obj['characteristics']['type']
    else:
        animal_type = "undefined"

    content += f"<strong>Type:</strong> {animal_type}<br/>"
    content += "</p>"
    content += "</li>"
    return content


def print_animals_data(data):
    """
    Serialize a list of animal objects into HTML content for printing.
    """
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def read_html(read_file):
    """
    Read content from the file.
    """
    with open(read_file, "r") as handle:
        return handle.read()


def replace_animals_info(output, html_temp):
    """
    Replace the placeholder in the HTML template with the animal data.
    """
    return html_temp.replace("__REPLACE_ANIMALS_INFO__", output)


def write_html(new_string, new_file):
    """
    Write content to an HTML file.
    """
    with open(new_file, "w") as handle:
        handle.write(new_string)


def main():


    animal_name = input("Enter the name of an animal: ").strip().lower()
    animal_data = data_fetcher.fetch_data(animal_name)

    if not animal_data:
        output = f"<h2>The animal {animal_name} doesn't exist.</h2>"
    else:
        output = print_animals_data(animal_data)

        print(output)

    html_temp = read_html("animals_template.html")
    new_string = replace_animals_info(output, html_temp)
    write_html(new_string, 'animals.html')


if __name__ == "__main__":
    main()