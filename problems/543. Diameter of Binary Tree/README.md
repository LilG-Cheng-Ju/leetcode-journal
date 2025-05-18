# 543. Diameter of Binary Tree 🟢

[🔗 543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)

## Description

Given the `root` of a binary tree, return the length of the diameter of the tree.
The **diameter** of a binary tree is the length of the longest path between `any two nodes` in a tree.
This **diameter** path may or may not pass through the `root`.

## Approach - DFS
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](./solution.py)

Although this problem is categorized as `EASY 🟢`, it's a great opportunity to deepen your understanding of the `Binary Tree` data structure and how `DFS (Depth-First Search)` works.

We recursively traverse each node in the tree using `DFS` and calculate the depth of its left and right children. Initialize `res` to 0 and update it with `max(res, left_depth + right_depth)` at each node — this captures the longest path (diameter) through the node.

The DFS function takes the current node and its depth as inputs. After computing the depth of the left and right subtrees, return `max(left_depth, right_depth) + 1`, which represents the maximum depth from the current node downwards.

At a leaf node, since both children are `None`, simply return the current depth.

## Time and Space Complexity
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)`

`n` represents the total number of nodes in the binary tree, and `h` is the height of the tree. Since we perform a depth-first search (DFS) and visit each node exactly once, the time complexity is `O(n)`. The space complexity is `O(h)` because the maximum depth of the recursion stack is equal to the height of the tree.