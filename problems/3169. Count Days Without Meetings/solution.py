from collections import defaultdict
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        schedule = defaultdict(int)
        
        for s, e in meetings:
            schedule[s] += 1
            schedule[e+1] -= 1

        prev_day = 1
        prefix_sum = 0
        ans = 0
        for d in sorted(schedule.keys()):
            if prefix_sum == 0:
                ans += d - prev_day
            prefix_sum += schedule[d]
            prev_day = d

        ans += days - prev_day + 1

        return ans

    