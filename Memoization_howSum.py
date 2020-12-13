def Bruteforce_howSum(targetSum, elements): 

  if targetSum==0: 
    return []
  
  if targetSum < 0:
    return None

  for i in range(len(elements)): 
    reminder = targetSum - elements[i]
    reminderResults = Bruteforce_howSum(reminder, elements)
    if reminderResults!=None: 
      return reminderResults + [elements[i]]

  return None     

def howSum(targetSum, elements, memo):

  if targetSum in memo: 
    return memo[targetSum]

  if targetSum == 0: 
    return [] 

  if targetSum < 0: 
    return None 

  for i in range(len(elements)): 
    reminder = targetSum - elements[i]
    reminderresult = howSum(reminder, elements, memo) 
    if reminderresult!=None:
      memo[targetSum] = reminderresult + [elements[i]]
      return memo[targetSum]

  memo[targetSum] = None
  return None    

memo = {}
print(howSum(7, [2,3], memo))
print(Bruteforce_howSum(7, [2,3]))

#Time Complexity before memoization (Brute Force)
#O(n^m*m)

#Time Complexity after  memoization (Brute Force)
#O(n*m*m) => O(n*m**2)
#Space Complexity before memoization 
#O(m)

#Space Complexity after memoization 
#O(m*m)