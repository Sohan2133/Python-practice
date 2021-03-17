if __name__ == '__main__':
    n=int(input("Enter the last digit of series: "))
    sum= 0
    for i in range (1,n+1, 2):
        sum=sum+i
    print("Summation of the series is %s" %(sum))