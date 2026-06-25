class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)                        # O(n) time, O(n) space

        bucket = [[] for _ in range(len(nums) + 1)]    # O(n) space
        for num, freq in freq_map.items():              # O(n) time
            bucket[freq].append(num)

        result = []
        for freq in range(len(bucket) - 1, 0, -1):     # O(n) time
            result.extend(bucket[freq])
            if len(result) >= k:
                return result[:k]

        return result
        