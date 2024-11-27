#while loop inside while loop breaking inner loop with inner loop value

i=1
while i<6:
    j=1
    while j<6:
        if j==3:
            break
        print(i,j)
        j+=1
    i+=1
