if __name__=="__main__":
    arr=list(map(int,input("Enter number ").split()))
    
    dp={}
    
    def helper(id):
        if id in dp:
            return dp[id]
        if id>=len(arr)-1:
            return 0
        ans=1000000
        
        for i in range(id+1,min(len(arr),id+arr[id]+1)):
            ans=min(ans,1+helper(i))
            
        dp[id]=ans
        return dp[id]        
    
    if helper(0)==1000000:
        print("No ans Exit")
    else:
        print(helper(0))
    