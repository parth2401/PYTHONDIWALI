Marks1 = int(input("Enter marks of physics"))
Marks2 = int(input("Enter marks of chemistry"))
Marks3 = int(input("Enter marks of biology "))
Marks4 = int(input("Enter marks of maths"))
Marks5 = int(input("Enter marks of cs"))
TOTAL = Marks1 + Marks2 + Marks3 + Marks4 + Marks5

percent = ((TOTAL)/500)*100 

if(percent >= 90) :
    print("GRADE A")
elif(percent >=80 and percent <=90):
    print("GRADE B")
elif(percent >=70 and percent <=80):
    print("GRADE C")
elif(percent >=60 and percent <=70):
    print("GRADE C ")
elif(percent >=50 and percent <=60):
    print("GRADE D ")
elif(percent >=40 and percent <=50):
    print("GRADE E")
elif(percent < 40): 
     print("GRADE F ")  
