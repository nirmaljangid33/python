class employe:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("jai hanuman ji")
    @staticmethod
    def hello():
        print("jai baba ki")

    def info(self,frist,last):
        self.frist = frist
        self.last = last
s= employe("nirmal",90)
print(s.name)
print(s.marks)
s.info("nirmal","jangid")
print(s.frist)
print(s.last)
s.hello()
