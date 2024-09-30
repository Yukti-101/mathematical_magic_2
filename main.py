from math import sqrt
number=int(input("Enter the number:"))
if number>1:
    for i in range(2,int(sqrt(number))+1):
        if(number%i==0):
            print("Number is not prime",number)
            break
    else:
            print("Number is a prime number",number)

else:
            print("Number is not a prime number",number)

            