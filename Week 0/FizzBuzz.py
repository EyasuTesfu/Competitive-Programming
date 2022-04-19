class Solution:
    def fizzBuzz(self, n: int):
        self.FizzBuzz = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.FizzBuzz.append("FizzBuzz")
            elif i % 3 == 0:
                self.FizzBuzz.append("Fizz")
            elif i % 5 == 0:
                self.FizzBuzz.append("Buzz")
            else:
                self.FizzBuzz.append(str(i))
        return self.FizzBuzz


n = 3
print(Solution.fizzBuzz(Solution, n))
