# problem link:https://leetcode.com/problems/convert-the-temperature/description/
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        ans = [Kelvin, Fahrenheit]
        return ans
