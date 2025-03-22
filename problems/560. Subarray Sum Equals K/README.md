# 560. Subarray Sum Equals K 🟡

[🔗 560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k)

## Description
Given an 1D array of integer `nums` and a integer `k`, find the number of subarrays in `nums` whose sum equals to `k`.

## Approach - Prefix Sum with Hash map
[![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](solution.cpp)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](solution.py)

Iterate through the `nums` and maintain a integer `prefix_sum`, and using a hashmap `prefix_sum_count` to track the frequency of each `prefix_sum`. Additionally, initialize an integer `ans = 0` to store the final answer.

For each number in `nums`, add the number to `prefix_sum` and increment the `prefix_sum_count[prefix_sum]` by 1. If `prefix_sum - k` exists in `prefix_sum_count` -- it means there are `prefix_sum_count[prefix_sum]` valid subarrays(becouse the difference between `prefix sum j` and `prefix sum i` is equal to **the sum of `nums[i:j]`**). In this case, update the `ans` by adding `prefix_sum_count[prefix_sum]` to it.

After iterating through all the numbers in `nums`, return `ans`.

## Time and Space Complexity
- **Time Comlexity**: `O(n)`
- **Space Complexity**: `O(n)`

where `n = length of nums`


