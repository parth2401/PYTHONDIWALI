def product(a,b):
    if(a<b):
        return product(b,a)
    elif(b!=0):
        return(a+product(a,b-1))
    else:
        return 0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Product is: ",product(a,b))

OUTPUT :-
Enter first number: 56
Enter second number: 35
Product is:  1960
