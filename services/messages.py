import os
import json

# loads all languages
messages_in_all_languages = {}
for i in os.listdir('./languages'):
    if i.endswith('.json'):
        with open(os.path.join('./languages', i)) as file:
            response = json.load(file)
        messages_in_all_languages[i.strip('.json')] = response


def get_lang(language, message_id):
    return messages_in_all_languages[language][message_id]
