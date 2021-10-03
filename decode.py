text = input("enter encrypted word: ")

deciphered_word = ''

for char in text:
    if not char.isalpha():
        continue
    new_char = char.lower()
    uni_code = ord(new_char) - 1
    if uni_code < ord('A'):
        uni_code = ord('Z')
    deciphered_word += chr(uni_code)

print(deciphered_word)


