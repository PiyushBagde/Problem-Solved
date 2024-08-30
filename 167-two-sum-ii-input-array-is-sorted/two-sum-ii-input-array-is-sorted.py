class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):

            high = len(numbers) - 1
            low = i+1

            while low <= high:
                val = target - numbers[i]
                mid = (low+high)//2
                if numbers[mid] == val:
                    return [i+1, mid+1]
                elif val < numbers[mid]:
                    high = mid-1
                else:
                    low = mid+1
                



        