numbers_string = input("Enter numbers separated with spaces: ")
numbers = numbers_string.split()
total_sum = 0

try:
    for number in numbers:
        total_sum += int(number)
    print('the total sum of numbers is ', total_sum)
except:
    print(number, 'is not a number')

