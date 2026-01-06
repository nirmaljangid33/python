with open("E:/python/file/prectice.txt","r") as f:
    data = f.read()
    new_data = data.replace("python","nirmal")
    print(new_data)