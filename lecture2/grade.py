mark=int(input("give a positive number:"))

if mark > 100 or mark < 0:
    print("Wrong input")
elif mark>=80:
    print("it is A+")
elif mark>=70:
    print("it is A")
elif mark>=60:
    print("it is A-")
elif mark>=50:
    print("it is B")
elif mark >= 40:
    print("it is C")
elif mark >= 33:
    print("it is D")
else:
    print("it is fail")

