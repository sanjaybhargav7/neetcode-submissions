class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for rp in range(len(nums)-1):
            wp = rp+1
            while wp < len(nums):
                if(nums[rp]+nums[wp] == target):
                    return [rp,wp]
                wp +=1
        

            
        