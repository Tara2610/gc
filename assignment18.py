#1. write a program to print the grade of a student based on the marks obtained.
"""
marks=int(input("Enter the marks:"))
if marks>96:
    print("Grade is A+.")
elif marks>92 and marks<97:
    print("Grade is A.")
elif marks>89 and marks<93:
    print("Grade is A-.")
elif marks>86 and marks<90:
    print("Grade is B+.")
elif marks>82 and marks<87:
    print("Grade is B.")
elif marks>79 and marks<83:
    print("Grade is B-.")
elif marks>76 and marks<80:
    print("Grade is C+.")
elif marks>72 and marks<77:
    print("Grade is C.")
elif marks>69 and marks<73:
    print("Grade is C-.")
elif marks>66 and marks<70:
    print("Grade is D+.")
elif marks>64 and marks<67:
    print("Grade is D.")
else:
    print("F")
"""

#2. Write a program to print if the guven year is leap or not.
"""
year=int(input("Enter the year:"))
if year%4==0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
"""

#3. Write a program to print if the given number is zero or odd or even.
"""
a=int(input("Enter a number:"))
if a==0:
    print("Given number is zero.")
elif a%2==0:
    print("Given number is even.")
elif a%2!=0:
    print("Given number is odd.")
"""
#4. Write a program to check the strength of a password.(please provide different rules for the password)
Password=input("Enter the password:")
list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list3=['!','@','#','$','%','^','&','*']
list4=[0,1,2,3,4,5,6,7,8,9]
if len(Password)>8:
    if Password in list1 and Password in list2 and Password in list3 and Password in list4:
        print("Strong password")
    else:
        print("Weak password")
else:
    print("Password must contain an uppercase letter, lowercase letter, special character and a number.")

#5. Write a program to create a calculator that perform basic arithematic operations.
"""
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
op=input("enter the operation:")
if op=='+':
    print("Sum of 2 numbers:",a+b)
elif op=='-':
    print("subtraction of 2 numbers:",a-b)
elif op=='*':
    print("product of 2 numbers:",a*b)
elif op=='/':
    print("division of 2 numbers:",a/b)
elif op=='%':
    print("modulo(remainder) of 2 numbers:",a%b)
"""