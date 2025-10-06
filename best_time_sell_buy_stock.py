if __name__=="__main__":
    prices=list(map(int,input("enter the list of prices").split()))
    
    def maxProfit(prices):
        ans=0
        curr_price=prices[0]
        for i in range(1,len(prices)):
            ans=max(ans,prices[i]-curr_price)
            if prices[i]<curr_price:
                curr_price=prices[i]
        return ans
    print(maxProfit(prices))