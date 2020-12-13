def gridtraversal(m,n, memo):

  if m==0 or n==0: 
    return 0 

  if m==1 and n==1:
    return 1 

  memo[(m,n)] = gridtraversal(m-1, n, memo) + gridtraversal(m, n-1, memo)
  return memo[(m,n)]    

memo = {}
gridtraversal(3,3,memo)