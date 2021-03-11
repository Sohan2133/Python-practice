year=int(input("give a year"))
if year%400==0:
    print(" the year is leap year:")
elif year%4==0 and year%100!=0:
    print(" the year is leap year")
else:
    print("the year is not leap year")