#while loop inside for loop breaking inner loop with outer loop value

for i in range(1,6):
    j=1
    while j<6:
        if i==3:
            break
        print(i,j)
        j+=1
