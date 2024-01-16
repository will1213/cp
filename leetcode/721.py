class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        a = defaultdict(set)
        n = defaultdict(str)
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i in range(len(emails)):
                for e in emails:
                    a[emails[i]].add(e)
                n[emails[i]] = name
        ans = []
        visited = set()
        q = deque()
        for e1, e2 in a.items():
            if e1 not in visited:
                temp = set()
                q.append(e1)
                while q:
                    email = q.popleft()
                    if email not in visited:
                        visited.add(email)
                        temp.add(email)
                        for e in a[email]:
                            temp.add(e)
                            q.append(e)
                ans.append([n[e1]] + sorted(list(temp)))
        return ans
