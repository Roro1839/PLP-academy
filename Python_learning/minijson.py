import json
from difflib import get_close_matches

def load_dictionary():
    """Load the dictionary dat from a JSON file."""
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def normalize_word(word):
    """Normalize the word to lowercase."""
    return word.lower()

def get_definition(word, dictionary):
    """Return the definition of a word."""
    normalize_word = normalize_word(word)
    definitions = dictionary.get(normalize_word, [])
    if definitions:
        return definitions
    else:
        return "Word not found."

def suggest_correction(word, dictionary):
    """Suggest a correction for a misspelled word."""
    normalized_word = normalize_word(word)
    matches = get_close_matches(normalized_word, dictionary.keys())
    if matches:
        return f"Did you mean '{matches[0]}'?"
    else:
        return "No suggestions."

def main():
    dictionary = load_dictionary()

    word = input("Enter a word: ").strip()
    print("\nDefinition:")
    print(get_definition(word, dictionary))

    print("\nCorrection Suggestion:")
    print(suggest_correction(word, dictionary))

if __name__ == "__main__":
    main()
