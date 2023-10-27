#Find Leap Year 
#Condition is divisible by 4, if div by 4 and also div by 100 its not a leap, if div by 4 and div by 100 but also div by 400 its leap year

leap_year = int(input("Enter a year to find leap year: "))
if leap_year%4==0:
    if leap_year%100 == 0:
        if leap_year % 400 == 0:
            print("Yes, Its a Leap Year")
        else:
            print("No, Its not a Leap Year")
    else:
        print("Yes, Its a Leap Year")
else:
    print("No, Its not a Leap Year")
