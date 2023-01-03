
def searches(arr, target):      #call function
  for i in range(len(arr)):       # run for loop, run index one-by-one and incerement i++, until we find our target which is 3
    if arr[i] == target:            # once we find target return the index or i
      return i
    else:
      continue
      
arr= [1, 2, 3, 4, 5]
target = 3
print(searches(arr, target))

