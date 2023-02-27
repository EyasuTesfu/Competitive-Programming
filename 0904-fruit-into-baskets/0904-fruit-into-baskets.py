class Solution:
    def totalFruit(self, fruits: List[int]) -> int: 
        baskets = {}
        count = 0
        left = 0
        for right in range(len(fruits)):
            if fruits[right] not in baskets:
                if len(baskets) == 2:
                    # move left next to the last index of the dropped fruit and drop fruit
                    _min = len(fruits)
                    for fruit in baskets:
                        _min = min(_min, baskets[fruit])
                    rem_fruit_ind = 0
                    for fruit in baskets:
                        if baskets[fruit] == _min:
                            rem_fruit_ind = fruit
                    left = baskets[rem_fruit_ind] + 1
                    del baskets[rem_fruit_ind]
                    
            count =  max(count, right-left+1)
            baskets[fruits[right]] = right
        return count