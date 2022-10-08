# Write a python script to use NOT IN operator to display the data not present in list.
list,n,i=[],int(input("How many  data items you want to store in a list : ")),0
while(i<n):
    list.append(input("Enter the value in list : "))
    i=i+1
data=input("Enter the value of data which you want to search in : ")
print("Not present! ") if data not in list else print("Yes present! ")