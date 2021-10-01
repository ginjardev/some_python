def my_split(string):
    if string == '' or string.isspace():
        return []

    list = []
    word = ''
    inword = not string[0].isspace()

    for x in string:
        if inword:
            if not x.isspace():
                word = word + x
            else:
                list.append(word)
                inword = False
        else:
            if not x.isspace():
                inword = True
                word = x

            else: 
                pass
    if inword:
        list.append(word)

    return list


print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))