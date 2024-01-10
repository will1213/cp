class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(list)
        prev = s[0]
        counter = 1
        count[1].append(prev)
        for i in range(1, len(s)):
            if s[i] == prev:
                counter += 1
                for j in range(1, counter):
                    count[j].append(s[i])
            else:
                prev = s[i]
                counter = 1
            count[counter].append(s[i])
        while count:
            maxSpecial = max(count)
            temp = Counter(count[maxSpecial])
            for v in temp.values():
                if v >= 3:
                    return maxSpecial
            del count[maxSpecial]
        return -1
            