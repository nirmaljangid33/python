number = [1, 2, 3, 2, 1]

number2 = number.copy()
number2.reverse()

if number == number2:
    print("This is a palindrome number")
else:
    print("Not a palindrome number")
