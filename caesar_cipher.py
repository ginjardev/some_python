word_to_encrypt = input('Enter a word or phrase to encrypt: ')

encrypted_word = ''
for word in word_to_encrypt:
    if not word.isalpha():
        continue
    capitalized_word = word.upper()
    uni_code = ord(capitalized_word) + 1
    if uni_code > ord('Z'):
        uni_code = ord('A')
    encrypted_word += chr(uni_code)
    
print(encrypted_word)



