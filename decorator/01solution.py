def greet(fx):
    def inner():
        print("Program start :")
        fx()
        print("Program End ? ")
    return inner

@greet
def hello():
    print("hello  byy....")

hello()
