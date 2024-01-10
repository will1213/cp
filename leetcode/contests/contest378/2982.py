class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(list)
        prev = s[0]
        counter = 1
        count[1].append(prev)
        for i in range(1, len(s)):
            if s[i] == prev:
                counter += 1
            else:
                prev = s[i]
                counter = 1
            count[counter].append(s[i])
        biggest = max(count)
        while count:
            maxSpecial = max(count)
            temp = Counter(count[maxSpecial])
            for k, v in temp.items():
                if maxSpecial > 1:
                    for j in range(biggest-maxSpecial+1):
                        count[maxSpecial-1].append(k)
                if v >= 3:
                    return maxSpecial
            del count[maxSpecial]
        return -1
            