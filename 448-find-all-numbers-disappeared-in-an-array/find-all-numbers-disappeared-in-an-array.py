class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []            

        def search(nums, key):
            low = 0 
            high = len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] == i:
                    return True
                elif i < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1

            return False

            

        for i in range(1, len(nums)+1):
            if search(nums,i) == False:
                res.append(i)
                
        return res


        