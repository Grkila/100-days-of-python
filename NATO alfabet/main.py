
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas
NATO_csv=pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_dict={ rows.letter: rows.code for (index,rows) in NATO_csv.iterrows()}

word=input("Enter a word: ").upper()
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

solution=[NATO_dict[letter] for letter in word]
print(solution)