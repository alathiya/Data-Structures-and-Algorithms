def canSum(targetSum, elements, memo):

  if targetSum in memo: 
    return memo[targetSum]

  if targetSum == 0: 
    return True 

  if targetSum < 0: 
    return False 

  for i in range(len(elements)): 
    reminder = targetSum - elements[i]
    if canSum(reminder, elements, memo) == True: 
      memo[targetSum] = True
      return True

  memo[targetSum] = False
  return False    

memo = {}
canSum(300, [7, 14], memo)

