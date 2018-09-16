# O(n^2) time
# O(1)
def insertionsort(lst):
  size=len(lst)
  for i in xrange(size):
    curr=lst[i]
    j=i-1
    while j>=0 and lst[j]>curr:
      lst[j+1]=lst[j]
      j-=1
    lst[j+1]=curr
  return lst

if __name__ == '__main__':
  print insertionsort([4,2,8,5,1])
