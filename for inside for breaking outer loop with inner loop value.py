#for loop inside for loop breaking outer loop with inner loop value

for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==5:
        break

'''
iteration
1.controller will take 1 from the outer loop and it will enter to the inner loop
  and controller will take 1 from the inner loop and printing 1,1 and traversing
  initialization will happen and j value will become 2
2.it will take 2 from the inner loop and printing 1,2 and traversing and initialization
  will happen and j value will become 3
3.it will take 3 from the inner loop and printing 1,3 and traversing and initialization
  will happen and j value will become 4
4.it will take 4 from the inner loop and printing 1,4 and traversing and initialization
  will happen and j value will become 5
5.it will take 5 from the inner loop and printing 1,5.after that there is no element
  in inner loop so controller will come out of the inner loop.controller will check
  the condition if j is equals to 5 or not.if it equal then it will break.here j
  value is 5 so outer loop will break and controller will come out of the loop

'''


