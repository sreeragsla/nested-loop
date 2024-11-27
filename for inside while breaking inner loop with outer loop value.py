#for loop inside while loop breaking inner loop with outer loop value

i=1
while i<6:
    for j in range(1,6):
        if i==3:
            break
        print(i,j)
    i+=1
