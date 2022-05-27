
###############tried to implement by recursion but got locked in the maze########################
# class Solution:
#     def evalRPN(self, tokens: list[str], stack=[]) -> int:
#         ans = 0
#         operators = ["+", "-", "*", "/"]
#         print(tokens)
#         if len(tokens) == 0:
#             return 0
#         elif len(tokens) < 2:
#             # print("here")
#             # print(eval(str(tokens[0] + stack[0] + tokens[1])))
#             # return eval(str(tokens[0] + stack.pop() + tokens[1]))
#             return int(tokens[-1])
#         elif tokens[-1] not in operators:
#             # ans = eval(str(tokens[-2] + stack.pop() + tokens[-1]))
#             print(stack, "stack")
#             print(tokens, "tokens")
#             if tokens[-2] not in operators:
#                 last_operator = stack.pop()
#                 result = eval(str(tokens[-2] + last_operator + tokens[-1]))
#                 last_operator = stack[-1]
#                 print(eval(str(str(self.evalRPN(
#                     self, tokens[:-2], stack=stack)) + last_operator + str(result))), "eval-in")
#                 return eval(str(str(self.evalRPN(self, tokens[:-2], stack=stack)) + last_operator + str(result)))
#             else:
#                 last_operator = stack.pop()
#                 return eval(str(str(self.evalRPN(self, tokens[:-1], stack=stack)) + last_operator + tokens[-1]))
#         else:
#             if tokens[-1] == '/':
#                 stack.append("//")
#             else:
#                 stack.append(tokens[-1])
#             print(stack, "stack-else")
#             return self.evalRPN(self, tokens[:-1], stack)


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                result = str(int(eval(str(stack[-2] + tokens[i] + stack[-1]))))
                stack.pop()
                stack.pop()
                stack.append(result)
        return result


token = ["4", "13", "5", "/", "+"]
print(Solution.evalRPN(Solution, tokens=token))
token = ["2", "1", "+", "3", "*"]
print(Solution.evalRPN(Solution, tokens=token))
token = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution.evalRPN(Solution, tokens=token))
