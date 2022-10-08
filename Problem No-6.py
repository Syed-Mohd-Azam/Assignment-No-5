# Write a python script which takes a three digit number from the user and displays only its middle digit.
n=int(input("Enter a three digit number: "))
print("Middle digit of a three digit number :",(n//10)%10) if 99<n<1000 else print("Not a three digit number!")