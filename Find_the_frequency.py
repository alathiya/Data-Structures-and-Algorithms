#User function Template for python3

"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""

from collections import defaultdict
def findFrequency (arr, n, x):
    # Your Code Here
    
    hashmap = defaultdict(int)
    for i in range(n): 
        hashmap[arr[i]] += 1
    
    if x in hashmap:
        return hashmap[x]
    else:
        return 0


#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list (map (int, input ().split ()))
    x = int (input ())
    
    print (findFrequency (arr, n, x))
    

# } Driver Code Ends