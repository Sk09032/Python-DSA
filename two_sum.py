def two_sum(nums, target):
    num_map = {}
    for i , num in enumerate(nums):
        finder=target-num
        if finder in num_map:
            return [num_map[finder],i]
        num_map[num]=i
    return []
if __name__ == "__main__":
    
    numbers=list(map(int,input("Enter the list of numbers seperated by space: ").split()))
    target=int(input("Enter the target number: "))
    
    result = two_sum(numbers, target)

    if result:
        print(f"Indices of the two numbers that add up to {target} are: {result}")
    else:
        print("No two numbers add up to the target.")