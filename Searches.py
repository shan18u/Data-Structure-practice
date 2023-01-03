#Linear Search
def searches(arr, target):      #call function
  for i in range(len(arr)):       # run for loop, run index one-by-one and incerement i++, until we find our target which is 3
    if arr[i] == target:            # once we find target return the index or i
      return i
    else:
      continue
      
arr= [2, 1, 3, 6, 5, 4]
target = 3
print(searches(arr, target))


# Binary Search          Array is already sorted before it starts search
def searches(arr, start, end, target):          # call the function
  while (start <= end):                            # if start is < or = end, make mid
    mid = (start + end) // 2                      
      
    if mid > target:                                  # if mid > target, then start arr from right bcz array is already sorted unlike linear
      start = mid + 1
      
    elseif mid < target:
      start = mid - 1
      
    else:
      return mid
    
return start                                   # return the answer that we go from either if or elseif

arr= [1, 2, 3, 4, 5]
target = 3
print(searches(arr, 0, len(arr) -1, target))        # arr, i = 0, i = last index, 3

#binary in recurssion is 

   
    if mid > target:                                  # start from mid and end at end or move to right and start searching from right to left.
      searches(arr, mid + 1, end, target) 
      
    elseif mid < target:
      searches(arr, start, mid - 1, target)             # start from start and end at mid or move to left and start searching from left to right.
      
      
      
#Bubble Sorting
def bubble_sort(A):
  iteration_count = 0
    for i in range(len(A)):
      for j in range(len(A) - i - 1)                # when i = 0 then j = 0,1, 2, 3..., then i = 2, j = 0,1, 2...(won't run the last index from last time), 
                                                        #keep going until either we reach i = len(A) or we get sorted list done. 
        iteration += 1
          if A[J] > A[J +1]
            A[J], A[J + 1] = A[J + 1] , A[J]        #Swap these two 
   
  return A, iteration_count

A = [5. 3, 2, 1]
print(bubble_sort(A))

#Insertion sort
 def insertion_sort(A)
  for j in range (1, len(A)):
    key = A[j]                      # variable key 
    i = j - 1                           # pointer assign to the left of the key
    while i >= 0 and A[i] > key:          # as long as i > 0 and i > key 
      A[i + 1] = A[i]                       # move larger key to the right and move downwards and put small elements to the left
      i -= 1                                   # and move downwards and put small elements to the left 
    A[i + 1] = key
 return A
    
A = [5. 3, 2, 1]
print(insertion(A))






