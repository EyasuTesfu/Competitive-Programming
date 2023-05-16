class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ing_map = defaultdict(list)
        incoming = defaultdict(set)
        for recipe, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                ing_map[ing].append(recipe)
                incoming[recipe].add(ing)
        
        queue = deque()
        for ing in supplies:
            queue.append(ing)
        
        res = []
        while queue:
            ing = queue.popleft()
            for rec in ing_map[ing]:
                incoming[rec].remove(ing)
                if not incoming[rec]:
                    queue.append(rec)
                    res.append(rec)
        return res