try:
    number1 = int(input("enter the number : "))
    number2 = int(input("enter the number : "))
    print(number1 / number2)

except ZeroDivisionError:
    print("zero allowed nahi hai")

except ValueError:
    print("sirf number hi enter karo")

else:
    print("calculation complete ho gya hai sir ji.")

finally:
    print("hame kon rok sakta hai")
