if __name__ == '__main__':

    a=int(input("take a number: "))
    b=int(input("take a number: "))
    c=int(input("take a number: "))
    d=int(input("take a number: "))
    if a<b:
        if b<c:
            if c < d:
                print(" sorting as ascending is %s, %s, %s and %s "% (a, b, c, d))

            else:
                print(" sorting as ascending is %s , %s, %s and %s" %(a, b, d, c))

    if b<a:
        if a<c:
            if c<d:
                print(" sorting as ascending is %s , %s, %s and %s" % (b, a, c, d))
            else:
                print(" sorting as ascending is %s , %s, %s and %s" % (a, b, d, c))

    if c < a:
        if a < b:
            if b < d:
                print(" sorting as ascending is %s , %s, %s and %s" % (c, a, b,d))
            else:
                print(" sorting as ascending is %s , %s, %s and %s" % (c, a, d, b))
    if d < a:
        if a < c:
            if c < b:
                print(" sorting as ascending is %s , %s, %s and %s" % (d, a, c, b))
            else:
                print(" sorting as ascending is %s , %s, %s and %s" % (d, a, b, c))

