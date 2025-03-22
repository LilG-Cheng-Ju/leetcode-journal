# 437. Path Sum III 🟡

[🔗 437. Path Sum III](https://leetcode.com/problems/path-sum-iii/description/)

## Description
Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

## Approach - Prefix Sum with DFS + Hash map
[![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)](solution.cpp)

`ans` keeps track of the number of valid paths.
Use a `hashMap` to store prefix sums encountered during DFS traversal.

For each node in the **DFS** traversal:
1.	Update the `curSum` from the root.
2.	Check if `curSum - targetSum` exists in the `hashMap`.
	- If found, add its count to `ans`.
3.	Store `curSum` in the `hash map`, increasing its count.
4.	Recursively traverse the left and right subtrees.
5.	After returning from recursion (backtrack), **remove** one occurrence of `curSum` from the `hashMap` to ensure correctness for other paths.

Return `ans`.

## Time and Space Complexity
- **Time Comlexity**: `O(n)`
- **Space Complexity**: `O(n)`

where `n = the number of nodes`


