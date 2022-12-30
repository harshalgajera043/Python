#caeser cipher
# from art import logo
# print(logo)
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Modify the list such a way that in any scenario INDEXERROR don't show
#here we used three A to Z series such a way that middle series become the major series to encode. But whlie decoding as the index is positively shifted index out of limit error  can be pop-up to tackle that we have added another A to Z series
#same issue can be found after first decode to tackle that we have add A to Z series in the begining
#to access the middle series we have add 26 in our all indexs of list alphabet because use of alphabet.index(letter) will return the first index of letter but to operate on 2nd A to Z list we have to add 26 in index.

#encode
# def encrypt(plain_text, positive_shift):
#     list_new_letter = []
#     for letter in plain_text:
#         new_index = alphabet.index(letter) + positive_shift + 26
#         list_new_letter.append(alphabet[new_index])
#     # print(new_index)
#     # print(list_new_letter)
#     code_text = ""
#     for char in list_new_letter:
#         code_text += char
#     print(code_text)

# #decode
# def decrypt(cipher_text, negetive_shift):
#     list_new_letter = []
#     for letter in cipher_text:
#         new_index = alphabet.index(letter) - negetive_shift + 26
#         list_new_letter.append(alphabet[new_index])
#     # print(new_index)
#     # print(list_new_letter)
#     code_text = ""
#     for char in list_new_letter:
#         code_text += char
#     print(code_text)

def ceaser(text,shift,direction):
    list_new_letter = ""
    if direction == "encode":
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift + 26
                list_new_letter += alphabet[new_position]
            else:
                 list_new_letter += letter #No change
    elif direction == "decode":
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift + 26
                list_new_letter += alphabet[new_position]
            else:
                list_new_letter += letter #No change
    print(list_new_letter)
    
             

#use of while loop for continuously repeat while loop until user don't refuse to encode/decode
further_continue = True
while further_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    shift = shift_input%26
    # if direction == "encode":
    #     encrypt(plain_text=text,positive_shift=shift)
    # elif direction == "decode":
    #     decrypt(cipher_text=text,negetive_shift=shift)
    ceaser(text,shift,direction)
    further_continue = input("Do you want to continue?yes/no\n").lower()
    if further_continue == "No".lower():
        further_continue == False
        print("Goodbye")