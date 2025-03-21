from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[prefix_sum] += 1
        ans = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_sum_count:
                ans += prefix_sum_count[prefix_sum-k]
            prefix_sum_count[prefix_sum] += 1
        return ans