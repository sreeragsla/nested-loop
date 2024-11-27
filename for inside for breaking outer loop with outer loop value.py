#for loop inside for loop breaking outer loop with outer loop value

for i in range(1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
    
'''
iteration
1.controller will take 1 and it will check if 1 is equals to 3 or not.it is not
  equal so controller will enter into the inner loop and j will take 1 and printing
  1,1.after that traversing and initialization will happen and j value will become
  2
2.j will take 2 and printing 1,2 and traversing,initialization will happen and j
  value will become 3
3.j will take 3 and printing 1,3 and traversing,initialization will happen and j
  value will become 4
4.j will take 4 and printing 1,4 and traversing,initialization will happen and j
  value will become 5
5.j will take 5 and printing 1,5.after that there is no element so controller will
  come out of the inner loop and traversing and initialization will happen and i
  value will become 2
6.i will take 2 and it will check if 2 is equals to 3 or not. it is not equal so
  controller will enter to the inner loop and j will take 1 and printing 1,1 and
  traversing and initialization will happen and j value will become 2
7.j will take 2 and printing 2,2 and traversing,initialization will happen and j
  value will become 3
8.j will take 3 and printing 2,3 and traversing,initialization will happen and j
  value will become 4
9.j will take 4 and printing 2,4 and traversing,initialization will happen and j
  value will become 5
10.j will take 5 and printing 2,5.after that there is no element so controller will
  come out of the inner loop and traversing and initialization will happen and i
  value will become 3
11.i will take 3 and it will check if 3 is equals to 3 or not.it is equal so condition
  satisfies and outer loop will break and controller will come out of the loop

'''


