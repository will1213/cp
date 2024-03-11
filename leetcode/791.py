class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = defaultdict(int)
        ans = ''
        temp = ''
        orderSet = set(order)
        for c in s:
            if c in orderSet:
                counter[c] += 1
            else:
                temp += c
        for c in order:
            if c in counter:
                ans += c * counter[c]
        return ans + temp