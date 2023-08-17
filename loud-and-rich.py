class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_adj = defaultdict(list)
        for rich, poor in richer:
            richer_adj[poor].append(rich)
        answers = []
        queue = deque()
   
        for person in range(len(quiet)):
            _min = person
            queue = deque(richer_adj[person])
            vis = set()
            vis.add(person)
            while queue:
                rich = queue.popleft()
                vis.add(rich)
                if quiet[rich] < quiet[_min]:
                    _min = rich
                for rich_person in richer_adj[rich]:
                    if rich_person not in vis:
                        queue.append(rich_person)

            answers.append(_min)
        return answers