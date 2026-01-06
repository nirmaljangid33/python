f = open(r"E:\python\file\file.txt", "r")
data = f.readline()
data = f.readline()
print(data)
print(type(data)) 
f.close