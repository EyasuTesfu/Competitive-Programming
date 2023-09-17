class LockingTree:
    def __init__(self, parent: List[int]):
        self.locked = defaultdict(set) # locked someone
        self.locking_tree = defaultdict(set) # parent child relationship
        self.parent = parent
        self.locker = {} # has a locker
        for i in range(len(parent)):
            self.locking_tree[parent[i]].add(i)

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locker:
            self.locked[user].add(num)
            self.locker[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locker and self.locker[num] == user:
            del self.locker[num]
            self.locked[user].remove(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locker:
            return False
        
        # checks if node doesn't have a locked ancestor
        def dfs_up(node):
            if node == -1:
                return True
            # if true then ancestor is locked
            if node in self.locker:
                return False
            return dfs_up(self.parent[node])

        # checks if node has at least one locked descendant
        def dfs_down(node):
            # end means no locked descendant
            if node in self.locker:
                return True
            if not self.locking_tree[node]:
                return False
            # it has at least one locked descendant
            for child in self.locking_tree[node]:
                if dfs_down(child):
                    return True
            return False

        # unlocks all it's descendants
        def dfs_locker(node):
            if not self.locking_tree[node]:
                return
            for child in self.locking_tree[node]:
                if child in self.locker:
                    child_locker = self.locker[child]
                    self.locked[child_locker].remove(child)
                    del self.locker[child]
                dfs_locker(child)
        

        res_up = dfs_up(num)
        res_down = dfs_down(num)
        
        if res_up and res_down:
            self.locker[num] = user
            self.locked[user].add(num)
            dfs_locker(num)
            return True
        else:
            return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)