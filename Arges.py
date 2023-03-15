def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(2,2,2))
#More Args Function
def multiply(*arg):
    sum=1
    arg=list(arg)
    arg[0]=3
    for i in arg:
        sum*=i
    return sum
print(multiply(2,2,2))
#Kwargs
def hello(**kwargs):
    #print("Hello! My name is "+kwargs["first"]+" "+kwargs["last"])
    print("Hello",end=" ")
    for i,value in kwargs.items():
        print(i,end=" ")
hello(first="Siddharth",last="Rai")