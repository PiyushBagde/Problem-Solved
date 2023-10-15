nums = [1,2,3,4]
def getsum(nums):
    
    # solutin 1
    
    # result = 0
    # res = []
    # for num in nums:
    #     result+=num
    #     res.append(result)
        
    # return res
    
    # solution 2
    
    for i in range(len(nums) - 1):
        nums[i+1] += nums[i]
        
    return nums
    
print(getsum(nums))


    