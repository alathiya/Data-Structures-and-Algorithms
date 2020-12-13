def canConstruct(target, wordbank): 

  #base condition 
  if target == "":
    return True 

  for word in wordbank: 
    
    if target.startswith(word) == True: 
        suffix = target[len(word):]
        if canConstruct(suffix, wordbank) == True:
          return True 

  return False 


print(canConstruct('abcdef',['ab','abc','cd','def', 'abcd'])) 
print(canConstruct('skateboard',['bo','rd','ate','t', 'ska', 'sk', 'boar']))

# time complexity 
# O(n^m*m)

#space complexity 
# O(m*m)


def canConstruct(target, wordbank, memo): 

  if target in memo: 
    return memo[target] 

  if target == "":
    return True 

  for word in wordbank: 

    if target.startswith(word): 
      suffix = target[len(word):]
      if (canConstruct(suffix, wordbank, memo)) == True: 
        memo[target] = True
        return True
  
  memo[target] = False 
  return False

memo = {} 
print(canConstruct('abcdef',['ab','abc','cd','def', 'abcd'], memo)) 
print(canConstruct('skateboard',['bo','rd','ate','t', 'ska', 'sk', 'boar'], memo))

# time complexity 
# O(n*m*m)=> O(n*m^2)
# O(m*m)