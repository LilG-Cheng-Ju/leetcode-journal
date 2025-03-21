from typing import List
from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = set()
        supplies = set(supplies)
        indegree = {k:0 for k in recipes}
        lack_ingredient = defaultdict(list)

        for i, recipe in enumerate(recipes):
            requirements = ingredients[i]
            for r in requirements:
                if r not in supplies:
                    indegree[recipe] += 1
                    lack_ingredient[r].append(recipe)
        
        queue = deque([recipe for recipe, i in indegree.items() if i == 0])

        while queue:
            recipe = queue.popleft()
            res.add(recipe)

            for dependent in lack_ingredient[recipe]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)

        return list(res)