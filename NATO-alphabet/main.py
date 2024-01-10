import pandas as pd

# TODO 1. Create a dictionary in this format:
data = pd.read_csv("NATO-alphabet/nato_phonetic_alphabet.csv")

### Method 1 TO_DICT
# nato_dict = data.to_dict()
# letter_dict = nato_dict['letter']
# code_dict = nato_dict['code']
# formatted_nato_dict = {letter : code_dict[idx] for (idx, letter) in letter_dict.items()}

### Method 2 ITERROWS
formatted_nato_dict = {row.letter: row.code for (idx, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("Enter a word: ")
    word_list = [letter.capitalize() for letter in word]
    try:
        code_word_list = [formatted_nato_dict[letter] for letter in word_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_word_list)

generate_phonetic()
