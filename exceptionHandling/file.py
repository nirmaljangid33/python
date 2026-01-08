try:
    with open("E:\\python\\exceptionHandling\\new.txt", "r") as f:
        data = f.read()
        print("File content:")
        print(data)

except FileNotFoundError:
    print("File exist nahi karti")

finally:
    print("Program end ")
