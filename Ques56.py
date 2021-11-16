nl=[]
for x in range(100,500):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

OUTPUT :-
105,140,175,210,245,280,315,350,385,420,455,490
