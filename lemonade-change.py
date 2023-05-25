class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twentys = 0
        if len(bills) == 1 and bills[0] != 5:
            return False
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False
            else:
                twentys += 1
                if tens:
                    tens -= 1
                    if fives < 1:
                        return False
                    fives -= 1
                else:
                    if fives < 3:
                        return False
                    fives -= 3
        if fives < 0 or tens < 0:
            return False
        return True