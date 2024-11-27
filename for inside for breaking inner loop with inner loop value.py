#for inside for breaking inner loop with inner loop value

for i in range(1,6):
    for j in range(1,6):
        if j==3:
            break
        print(i,j)

'''
iteration
1.controller will take 1 from the outer loop and it will enter to the inner loop
  and j value will be 1 and it will check if 1 is equals to 3 or not.it is not equal
  so condition does not satisfies and printing 1,1 and traversing initialization
  will happen and j value will become 2
2.j will take 2 and it will check 2 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 1,2 and traversing initialization will happen
  and j value will become 3
3.j will take 3 and it will check 3 is equals to 3 or not.it is equal so condition
  satisfies and inner loop will break and controller will come out of the inner
  loop and traversing and initialization will happen and i value will become 2
4.i value will be 2 and controller will enter to the inner loop and j value will
  be 1 and it will check if 1 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 2,1 and traversing and initalization will happen
  and j value will become 2
5.j will take 2 and it will check 2 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 2,2 and traversing initialization will happen
  and j value will become 3
6.j will take 3 and it will check 3 is equals to 3 or not.it is equal so condition
  satisfies and inner loop will break and controller will come out of the inner
  loop and traversing and initialization will happen and i value will become 3
7.i value will be 3 and controller will enter to the inner loop and j value will
  be 1 and it will check if 1 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 3,1 and traversing and initalization will happen
  and j value will become 2
8.j will take 2 and it will check 2 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 3,2 and traversing initialization will happen
  and j value will become 3
9.j will take 3 and it will check 3 is equals to 3 or not.it is equal so condition
  satisfies and inner loop will break and controller will come out of the inner
  loop and traversing and initialization will happen and i value will become 4
10.i value will be 4 and controller will enter to the inner loop and j value will
  be 1 and it will check if 1 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 4,1 and traversing and initalization will happen
  and j value will become 2
11.j will take 2 and it will check 2 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 4,2 and traversing initialization will happen
  and j value will become 3
12.j will take 3 and it will check 3 is equals to 3 or not.it is equal so condition
  satisfies and inner loop will break and controller will come out of the inner
  loop and traversing and initialization will happen and i value will become 5
13.i value will be 5 and controller will enter to the inner loop and j value will
  be 1 and it will check if 1 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 5,1 and traversing and initalization will happen
  and j value will become 2
14.j will take 2 and it will check 2 is equals to 3 or not.it is not equal so condition
  does not satisfies and printing 5,2 and traversing initialization will happen
  and j value will become 3
15.j will take 3 and it will check 3 is equals to 3 or not.it is equal so condition
  satisfies and inner loop will break and controller will come out of the inner loop
  and there is no element in outer loop so controller will come out of the loop

'''



  
  
