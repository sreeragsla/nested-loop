#for loop inside while loop breaking outer loop with inner loop value

i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if j==5:
        break
    i+=1