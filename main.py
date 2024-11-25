import random


arrayA=[4, 5, 9, 75, 47, 79, 20, 74, 63 ,10]

def bubble_sort():
    n=len(arrayA)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arrayA[j]>arrayA[j+1]:
                arrayA[j], arrayA[j+1]=arrayA[j+1], arrayA[j]
        return arrayA
print(bubble_sort())


arrayB=[4, 8, 6, 9, 7, 45, 78, 10, 75, 89]

def is_sorted(arrayB):
    for i in range(1, len(arrayB)):
         if arrayB[i]<arrayB[1-1]:
             return False      
         return True

def bogosort (arrayB):
  count=0
  while not is_sorted(arrayB):
    random.shuffle(arrayB)
    count+=1
    print(f"Pokus(count): (arrayB)")
  print(f"seznam sežazen po (count) pokusech")

bogosort(arrayB)
print("bogo", arrayB)
    
      
