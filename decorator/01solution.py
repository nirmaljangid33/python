def greet(fx):
    def inner():
        print("jai hanuman ji :")
        fx()
        print("by by....")
    return inner

@greet
def hello():
    print("jai baba ki")

hello()
