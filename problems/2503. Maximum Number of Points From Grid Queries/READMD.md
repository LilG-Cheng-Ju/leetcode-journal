# 2503. Maximum Number of Points From Grid Queries 🔴

[🔗 2503. Maximum Number of Points From Grid Queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries)

## Description
Given an `m x n` integer matrix `grid` and an array `queries` of size `k`, compute an array `answer` where:

- Starting from `(0,0)`, for each `queries[i]`:
  - If `queries[i] > grid[x][y]` , in other words, `queries[i]` is **strictly greater** than the value of the current cell, gain **1 point** (only on the first visit) and move in 4 directions.
  - If `queries[i] <= grid[x][y]`, stop immediately.
- `answer[i]` is the maximum points earned.

Return the array `answer`.

## Approach - Sorting + BFS + heap
💡 **Use a min heap (priority queue) to explore cells in increasing order.**  
💡 **Sort `queries` to process in ascending order, ensuring each query builds upon the previous results, avoiding redundant searches.** 

### 🔹 Steps:  
1. **Sort `queries`** to process them in increasing order.  
2. **Min Heap for BFS traversal**  
   - Start from `(0,0)`, always expanding the smallest value first.  
3. **Process cells `< query[i]`**  
   - Pop from heap, gain **1 point**, and explore **4 neighbors**.  
   - Push unvisited neighbors into the heap.  
4. **Store results in `res`** and map each `query` to the current points.  
5. **Return results in original order** using `res[query]`.  

### ⏳ Complexity Analysis  
- **Time Complexity**: `O(m*n * log(m*n) + k log k)`  
  - Sorting `queries` takes `O(k log k)`, where `k` is the number of queries.  
  - Traversing the grid (each cell visited at most once) takes `O(mn)`, where `m` and `n` are grid dimensions.  
  - Each query processes heap operations in `O(log(mn))`, so the total heap operations remain `O(m*n * log(m*n))`.  

- **Space Complexity**: `O(mn + k)`  
  - `visited` and `heap` store up to `O(mn)` elements (each grid cell).  
  - `res` stores `O(k)` entries for query results.  
