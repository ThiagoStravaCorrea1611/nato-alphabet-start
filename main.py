# Import libraries
import pandas as pd

# Parameters
PATH_NATO_ALPHABET = "nato_phonetic_alphabet.csv"

# Open csv with phonetic alphabet
df_nato_phonetic_alphabet = pd.read_csv(PATH_NATO_ALPHABET)

# Nato phonetic alphabet dictionary
dict_nato_phonetic_alphabet = {row["letter"]:row["code"] for (index, row) in df_nato_phonetic_alphabet.iterrows()}

# While loop of app
translator_on = True
while translator_on:
    # Ask for user input
    user_input = input("A word to be translated: ").upper()
    
    # Check if it is time to quit
    if user_input == "EXIT":
        translator_on = False
        break
    
    # Translate user input to phonetic alphabet
    user_input_translated = [dict_nato_phonetic_alphabet[l] for l in user_input]
    
    print("-".join(user_input_translated))
