# Write a python script which takes a three digit number from the user and displays only its first digit.
n=int(input("Enter a three digit number : "))
print("First digit of three digit number is : ",n//100) if 100<=n<1000 else print("Not a three digit number! ")