import json
import requests

API_KEY = "I/qKGCs0oxX2XFwmfBo46A==whYupgYwUBaeWAdy"

# Funktion zum Erstellen des HTML-Codes für ein einzelnes Tier
def serialize_animal(animal_obj):
    output = ''  # define an empty string
    output += '<li class="cards__item">\n'

    # Name
    if 'name' in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    # Textblock starten
    output += '  <p class="card__text">\n'

    # Characteristics (kann fehlen)
    if 'characteristics' in animal_obj:
        characteristics = animal_obj['characteristics']

        if 'diet' in characteristics:
            output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
        if 'type' in characteristics:
            output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    # Locations (kann fehlen oder leer sein)
    if 'locations' in animal_obj and animal_obj['locations']:
        locations = ", ".join(animal_obj['locations'])
        output += f'      <strong>Location:</strong> {locations}<br/>\n'

    # Textblock und Listenelement schließen
    output += '  </p>\n'
    output += '</li>\n\n'

    return output


# Hauptfunktion
def main():
    #userinput for entering an animal name
    animal_to_search = input("What animal to search for? ").lower()
    #fetch the data from the API
    res = requests.get("https://api.api-ninjas.com/v1/animals", headers={"x-api-key": API_KEY}, params={"name": animal_to_search})
    data = res.json()
    print(data)

    if animal_to_search not in data[0]["name"].lower():
        print(f"The animal {animal_to_search} was not found. Please try again.")
    #create json file with the animal data
    with open("animals_data.json", "w") as animals_file:
        animals_file.write(json.dumps(data))

    # JSON-Datei lesen
    with open("animals_data.json", "r") as json_file:
        data = json.load(json_file)

    # HTML-Template lesen
    with open("animals_template.html", "r") as html_file:
        template_content = html_file.read()

    # Ausgabe aufbauen
    output = ''  # define an empty string
    for animal_data in data:
        output += serialize_animal(animal_data)

    # Platzhalter ersetzen
    new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # Neue Datei schreiben
    with open("animals.html", "w") as output_file:
        output_file.write(new_html)

    if animal_to_search in data[0]["name"].lower():
        print(f"Website was successfully generated for the animal: {animal_to_search}. You can find it under animals.html")


# Programm starten
if __name__ == "__main__":
    main()