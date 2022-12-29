alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Modify the list such a way that in any scenario INDEXERROR don't show
#here we used three A to Z series such a way that middle series become the major series to encode. But whlie decoding as the index is positively shifted index out of limit error  can be pop-up to tackle that we have added another A to Z series
#same issue can be found after first decode to tackle that we have add A to Z series in the begining
#to access the middle series we have add 26 in our all indexs of list alphabet because use of alphabet.index(letter) will return the first index of letter but to operate on 2nd A to Z list we have to add 26 in index.

#encode
def encrypt(text, shift):
    list_new_letter = []
    for letter in text:
        new_index = alphabet.index(letter) + shift + 26
        list_new_letter.append(alphabet[new_index])
    print(new_index)
    print(list_new_letter)
    code_text = ""
    for char in list_new_letter:
        code_text += char
    print(code_text)

#decode
def decrypt(text, shift):
    list_new_letter = []
    for letter in text:
        new_index = alphabet.index(letter) - shift + 26
        list_new_letter.append(alphabet[new_index])
    print(new_index)
    print(list_new_letter)
    code_text = ""
    for char in list_new_letter:
        code_text += char
    print(code_text)

#use of while loop for continuously repeat while loop until user don't refuse to encode/decode
further_continue = "yes"
while further_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    further_continue = input("Do you want to continue?yes/no\n").lower()