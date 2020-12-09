#code

def CheckPalindrome(S): 
    
    str1 = ""
    for i in range(len(S)):
        
        if str(S[i]).isalnum(): 
            str1 = str1 + str(S[i])
    
    
    str2 = ""
    for i in range(len(str1)-1, -1, -1):
        
        str2 = str2 + str(str1[i])     
    
    if str1.lower() == str2.lower():
        return "YES"
    else:
        return "NO" 
        
def main():    
    t = int(input ())
    for tc in range (t):
        S = str(input ())
        print(CheckPalindrome(S))
        

if __name__=="__main__":
    main()        