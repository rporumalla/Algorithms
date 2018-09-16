import math

# O(nlogn) time
# O(n) space
def mergesort(lst):
  if len(lst)==1:
    return lst

  mid=int(math.floor(len(lst)/2.0))
  left=lst[:mid]
  right=lst[mid:]
  
  return merge(mergesort(left), mergesort(right))

def merge(left, right):
  result=[]
  leftidx=0
  rightidx=0

  while (leftidx<len(left) and rightidx<len(right)):
    if left[leftidx]<right[rightidx]:
      result.append(left[leftidx])
      leftidx+=1
    else:
      result.append(right[rightidx])
      rightidx+=1

  return result+left[leftidx:]+right[rightidx:]

if __name__ == '__main__':
  print mergesort([6,4,1,5])

