if __name__ == '__main__':

    a=int(input("take a number: "))
    b=int(input("take a number: "))
    c=int(input("take a number: "))
    d=int(input("take a number: "))
    if a<b and a<c:
        if a<d:
            print("%s is minimum" %(a))
        else:
            print("%s is minimum" %(d))

    if b < a and b < d:
        if b < c:
            print("%s is minimum" % (b))
        else:
            print("%s is minimum" % (c))




