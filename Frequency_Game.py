from collections import defaultdict
A = [6,3,6,2,8,9,4,1,0,3,3,8,9,7]

N = len(A)

hashmap = defaultdict(int)

for i in range(N):  #O(n)
  hashmap[A[i]] += 1

hashmap = sorted(hashmap, reverse=True) # O(logn)

print(hashmap[0])