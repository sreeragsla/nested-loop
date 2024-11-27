#for loop inside while loop breaking inner loop with inner loop value

i=1
while i<6:
    for j in range(1,6):
        if j==3:
            break
        print(i,j)
    i+=1
