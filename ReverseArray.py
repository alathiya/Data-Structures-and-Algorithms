def ReverseArray(arr, n): 
    
    string = ""
    for i in range(n-1, -1,-1): 
        string = string + str(arr[i]) + ' '
    
    print(string)
    
def main():    
    t = int(input ())
    for tc in range (t):
        n = int(input ())
        arr = list (map (int, input ().split ()))
        ReverseArray(arr, n)
        

if __name__=="__main__":
    main()