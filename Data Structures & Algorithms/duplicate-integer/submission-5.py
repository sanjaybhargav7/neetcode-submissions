class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        b = True
        if len(nums) > 0:
            for char in nums:
                if res.get(char) is None:
                    res[char] = 1
                    b = False
                else:
                    res[char] += 1
                    b = True
                    break
        else:
            b = False
        return b
            
        