import pandas

alphabat = pandas.read_csv("nato_phonetic_alphabet.csv")
word_dict = {row.letter: row.code for (index, row) in alphabat.iterrows()}
# for (index, row) in alphabat.iterrows():
#     word_dict[row.letter] = row.code
print(word_dict)

user_name = input("what is your name? ").upper()
NATO_list = [word_dict[letter] for letter in user_name]

print(NATO_list)
