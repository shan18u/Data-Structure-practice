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
