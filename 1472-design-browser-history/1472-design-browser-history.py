class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head
        
    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node
        
        
    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.prev:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.curr.next:
            self.curr = self.curr.next
            i += 1
        return self.curr.val
        
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)