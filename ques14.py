a = int(input("Enter the age of first person"))
b = int(input("Enter the age of second  person"))
c = int(input("Enter the age of third  person"))
if ( a > b and a > c ) :
    print("a is oldest")
elif (b > a and b > c ):
    print("b is oldest")
elif (c > a and c > b):
    print("c is oldest")
else :
    print("all are equal")

Enter the age of first person99 
Enter the age of second  person53
Enter the age of third  person35
a is oldest 

Enter the age of first person 35
Enter the age of second  person 76
Enter the age of third  person44
b is oldest

Enter the age of first person 22 
Enter the age of second  person34 
Enter the age of third  person77 
c is oldest
