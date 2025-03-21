# 2115. Find All Possible Recipes from Given Supplies 🟡

[🔗 2115 ](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies)

## Description
Given a 1D array `recipes`, a 2D array `ingredients` and a 1D string array for strings `supplies`, where the recipe at `recipe[i]` can be created using the ingredients in `ingerdients[i]`, and `supplies` indicated the ingredients you initially have.
Return a *list of all the recipes* that you can create. 

## [Approach - Topological Sort](./solution.py)
Using **Kahn's Algorithm**, create a hashmap `indegree`  to represent the indegree of each recipe, and a hashmap of list `lack_ingredient`  to indicate the missing ingredients for each recipe. Also, use a set `res` to store eligible recipes.

For each recipe and its related ingredients, if any ingredient cannot be found in `supplies`, increment the indegree of the recipe by 1.

Next, add all recipes with an indegree of 0 to the `queue`. Then, perform a topological sort using Kahn's algorithm. If the indegree of a recipe becomes 0, add it to `res`.

After run though all 0-indegree recipes, return `res`.

## Time and Space Complexity
- **Time Comlexity**: `O(n+m+s)`
- **Space Complexity**: `O(n+m+s)`

where `n = num recipes`, `m = num of all ingredients` and `s = num supplies`


