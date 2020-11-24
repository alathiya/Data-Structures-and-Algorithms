arr = [9384,
887,
2778,
6916,
7794,
8336]
n = 6

lst = []

for i in range(n):
  lst.append(arr[i])

  lst = sorted(lst)

  if len(lst)% 2 == 0:
    print((lst[int(len(lst)/2)-1] + lst [int(len(lst)/2)])/2)
  else:
    print(lst[int(len(lst)/2)])   