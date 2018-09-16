#O(n^2) time
#O(1) space
def bubblesort(lst):
  swapped=True
  size = len(lst)
  while swapped:
    swapped=False
    for i in xrange(size):
      if i+1<size and lst[i] and lst[i+1] and lst[i]>lst[i+1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
	swapped=True	
  return lst

if __name__ == '__main__':
  print bubblesort([4,2,1,3])
