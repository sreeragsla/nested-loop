#while loop inside for loop breaking outer loop with outer loop value

for i in range(1,6):
    if i==3:
        break
    j=1
    while j<6:
        print(i,j)
        j+=1
