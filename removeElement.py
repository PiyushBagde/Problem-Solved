def removeElement( nums, val):
    i = 0 
    for n in nums:
        if n != val:
            nums[i] = n
            i+=1
            
    return i
            
print(removeElement(nums=[3,2,2,3], val= 3))
print(nums)
