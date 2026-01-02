def my_sum(*args):
    print(args) 
    for i in args: 
        print(i*9, end=' ')
    return sum(args)
print(my_sum(1,2,3,4,5))
