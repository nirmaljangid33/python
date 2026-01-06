with open("E:/python/file/prectice.txt","r") as f:
   data = f.read()
   num = ""
   for i in range(len(data)):
      if(data[i] ==","):
         num1 =int(num)
         if (num1%2==0):
            print(num1)
         num =""
      else:
         num +=data[i]