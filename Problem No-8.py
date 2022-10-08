# Write a python script to use IN operator to display the data present in the list.
list,n,i=[],int(input("How many values you want to store in list : ")),0
while(i<n):
    list.append(input("Enter the value in list: "))
    i=i+1
data=(input("Enter the value of data you want to search in: "))
print("Yes it is present! ") if data in list  else print("Sorry data item  is not present in the list !")