def bruteforce_bestSum(targetSum, elements): 
  #base case 
  if targetSum == 0: 
    return []

  if targetSum < 0: 
    return None 

  shortestSum = None

  for i in range(len(elements)): 
    reminder = targetSum - elements[i]
    results = bruteforce_bestSum(reminder, elements)
    if results!=None: 
         results = results + [elements[i]]

         if not shortestSum or len(results) < len(shortestSum):
           shortestSum = results

  return shortestSum        

#print(bruteforce_bestSum(7, [5,3,4,7]))
#print(bruteforce_bestSum(8, [2,3,5]))
#print(bruteforce_bestSum(7, [5,3,4,7]))
#print(bruteforce_bestSum(100, [1,2,5,25]))

#Brute Force
# time O(n^m*m)
# space O(m*m)


def bestSum(targetSum, elements, memo):

  if targetSum in memo: 
    return memo[targetSum]

  #base conditions 
  if targetSum == 0:
    return []

  if targetSum < 0:
    return None

  shortestSum = None 

  for i in range(len(elements)): 
    reminder = targetSum - elements[i]
    results = bestSum(reminder, elements, memo)
    if results != None: 
      results = results + [elements[i]]

      if not shortestSum or len(results) < len(shortestSum): 
        shortestSum = results

  memo[targetSum] = shortestSum
  return memo[targetSum]     

memo = {}
print(bestSum(100, [1,2,5,25], memo))

#memoized
# time O(n*m*m)
# space O(m*m)