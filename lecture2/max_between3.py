if __name__ == '__main__':

    a=int(input("take a number: "))
    b=int(input("take a number: "))
    c=int(input("take a number: "))
    if a==b==c:
        print("everybody are equal")
    elif a>b and a>c:
        print("%s is maximum between %s and %s " %(a,b,c))
    elif b>a and b>c:
        print("%s is maximum between %s and %s " % (b, a,c))
    else:
        print("%s is maximum between %s and %s " % (c, a,b ))


