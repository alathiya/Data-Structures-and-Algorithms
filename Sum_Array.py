def SumArray(arr, n): 
    
    sum_arr = 0
    for i in range(n):
        sum_arr = sum_arr + arr[i]    
    
    print(sum_arr)
    
def main():    
    t = int(input ())
    for tc in range (t):
        n = int(input ())
        arr = list (map (int, input ().split ()))
        SumArray(arr, n)
        

if __name__=="__main__":
    main()