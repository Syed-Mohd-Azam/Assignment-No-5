# Write a python script which takes a three digit number from the user and displays only its last digit.
n=int(input("Enter a three digit number: "))
print("Last digit of three digit number is : ",n%10) if 99<n<1000 else print("Not a three digit number! ")