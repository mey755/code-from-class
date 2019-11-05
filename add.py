def add(a,b,c):
    # print(a + b + c)
    theSum = a + b + c
    return theSum #intermediate value which is theSum
    # return a + b + c # number 6, called the function by signing the "result" to a varaible; a core concept


def main():
    # result = add(1,2,3) # order matters, everything is paired up 
    print(add(1,2,3)) #call a function within a print
    print(add(22,22,-100000))



main()