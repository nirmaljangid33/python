class student :
    def __init__(self,name,*marks):
        self.name =name
        self.marks = marks

    def avrage(self):
        total=0
        for m in self.marks:
            total += m
            return (total/len(self.marks))

s=student("nirmal" , 90,80,99)
print("Name : ",s.name)
print("Avrage : ",s.avrage())
