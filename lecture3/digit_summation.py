if __name__ == '__main__':
    num = int(input("Enter a number: "))
    hold=num
    sum=0
    while num > 0:
        rem= (num%10)
        sum= sum+rem
        num= int(num/10)

    print("Summation of digits of %s is %s" % (hold,sum))