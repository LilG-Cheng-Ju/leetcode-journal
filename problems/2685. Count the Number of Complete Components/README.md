# 2685. Count the Number of Complete Components 🟡

[🔗 2685. Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components)

## Description
Given an integer `n`, representing the number of vertices in an **undirected** graph (numbered from `0` to `n-1`), and a 2D integer array `edges` indicating the existing edges connecting these vertices, your task is to find the number of **Complete Components** in the graph.  

📌 A **connected component** is a subgraph in which there exists a path between any two vertices, and no vertex in the subgraph is connected to a vertex outside of it.  

🔹 **In simpler terms**, we need to find all **small groups** in the graph where every vertex within a group is directly connected to every other vertex in that group.  

## Approach - Union Find
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](./solution.py)

💡 In a **Complete Component**, every vertex is directly connected to every other vertex, meaning the total number of edges should be equal to `n(n-1)/2` where `n` is the number of vertices in that component.  

💡 Additionally, each vertex in a **Complete Component** should have exactly **`n-1`** neighbors (i.e., be connected to all other vertices in the group).  

### 🔹 Steps:
1. **Use Union-Find** (Disjoint Set Union) to identify all **connected components** in the graph.  
2. **Maintain a hashmap `adj_count`** to track the number of neighbors for each vertex while processing the edges.  
3. **After the Union-Find process**, use another hashmap `group` to group vertices that **share the same root** (i.e., belong to the same component).  
4. **For each identified group**, check if all its vertices have exactly `n-1` neighbors. Initialize an integer `ans` to 0 before counting.
   - If true ✅, it is a **Complete Component**, so we increment `ans`.  
   - If false ❌, it is not a Complete Component. 

After run though all connected components (**⚠️Note:** A vertex without edges is also considered a connected component.), return `ans`.

### ⏳ Complexity Analysis 
- **Time Complexity**: `{O(n+m))}` 
    - The `Union-Find` algorithm processes each edge in O(α(n)) time using path compression (where α is the inverse Ackermann function, nearly `O(1)`).
    - Iterating through all vertices and edges takes `O(n + m)`.
    - Checking each group requires at most `O(n)` operations.
    - Overall, the complexity is `O(n + m)`.


- **Space Complexity**: `{O(n)}`  
    We maintain two hashmaps (`adj_count` and `group`), each requiring `O(n)` space.

