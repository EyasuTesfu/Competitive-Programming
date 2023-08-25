class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.adj_list = defaultdict(list)
        self.currOrder = []

    def birth(self, parentName: str, childName: str) -> None:
        self.adj_list[parentName].append(childName)

    def death(self, name: str) -> None:
        self.adj_list[name].append("dead")

    def getInheritanceOrder(self) -> List[str]:
        self.buildOrder()
        return self.currOrder
    
    def buildOrder(self):
        self.currOrder = []
        def dfs(name):
            if "dead" not in self.adj_list[name]:
                self.currOrder.append(name)
            if not self.adj_list[name]:
                return
            for child in self.adj_list[name]:
                if child != "dead":
                    dfs(child)
        # print(self.adj_list)
        dfs(self.kingName)
            
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()