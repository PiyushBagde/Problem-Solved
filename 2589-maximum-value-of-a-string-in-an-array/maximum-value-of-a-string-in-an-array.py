class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        length = 0
        for ele in strs:
            if ele.isdigit():
                num = int(ele)
                if num > length:
                    length = num
            else:
                if len(ele)> length:
                    length = len(ele)
        return length


                
        