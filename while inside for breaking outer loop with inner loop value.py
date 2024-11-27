#while loop inside for loop breaking outer loop with inner loop value

for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break

    
