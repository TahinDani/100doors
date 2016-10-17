doors = ["C"]*100

for i in range(100):
    for x in range(i, 100, i+1):
        if doors[x]=="C":
           doors[x]="O"
        else:
            doors[x]="C"

print("The following doors are open: ", end="")
for i in range(100):
    if doors[i]=="O":
        door_numb=i+1
        print(door_numb, end=", ")
        '''Itt nagyon sokat próbálkoztam vele, hogy a legvégéről
        eltüntessem a ", "-t de se join-al se substringgel se 
        semmivel nem tudtam megcsinálni'''
print(end='\n')