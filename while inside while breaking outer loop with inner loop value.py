#while loop inside while loop breaking outer loop with inner loop value

i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break
    i+=1
