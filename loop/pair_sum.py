number = [2,7,11,15]
target = 9
for num in number:
    for n in number:
        if (num + n) == target:
            print(num, n)
            break
        else:
            print("targat is not match")
            break
        
        