class Solution:
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
        
        
    def solver(self)->bool:
        
        
        nums=self.nums
        target=self.target
        st,end=0,len(nums)-1
        
        
        while st<=end:
            mid=(st+end)//2 
            if nums[mid]==target:
                return True
            if nums[mid]>=nums[st]:
                if nums[st]<=target<nums[mid]:
                    end=mid-1
                else:
                    st=mid+1
            elif nums[mid]<=nums[end]:
                if nums[mid]<target<=nums[end]:
                    st=mid+1
                else:
                    end=mid-1
            else:
                st+=1
                
    
        return False
def main():
    s=[3,4,5,6,7,0,1,2]
    target=2
    solution=Solution(s,target)
    result=solution.solver()
    print(result)

if __name__=="__main__":
    main()