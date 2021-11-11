from os import strerror

# stream = open('text.txt', 'rt')
# counter = 0
# try:
#     ch = stream.read()
#     for i in ch:
#         print(i, end="")
#         counter += 1
# except IOError as e:
#     print(e.errno)

# print("\ncharacters in your text file are:", counter)

read_by_line = open('text.txt', 'rt')
lines = read_by_line.readline()
try:
    count = 0
    while  lines != '':
        print(lines)
        count += 1
        lines = read_by_line.readline()
    #read_by_line.close()
    print("lines in paragraph:", count)
except IOError as e:
    print(e.errno)