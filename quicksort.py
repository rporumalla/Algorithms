import random
import math

def partition(lst, left, right):
  pivot=int(math.floor(random.random()*(right-left+1)+left))
  while left<right:
    while lst[left]<lst[pivot]:
      left+=1
    while lst[right]>lst[pivot]:
      right-=1
    if left<right:
      lst[left],lst[right]=lst[right],lst[left]
  
  print left, pivot
  lst[left],lst[pivot]=lst[pivot],lst[left]
  print lst
  return left

def quicksort(lst, left, right):
  if left<right:
    pivot=partition(lst, left, right)
    quicksort(lst, left, pivot)
    quicksort(lst, pivot+1, right)

if __name__ == '__main__':
  arr=[1,5,4,2,3]
  quicksort(arr, 0, len(arr)-1)
  print arr
