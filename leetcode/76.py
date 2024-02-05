class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        p1 = 0
        p2 = 0
        ans = [0,len(s)]
        index = []
        match = 0
        for i in range(len(s)):
            if s[i] in counter:
                index.append(i)
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    match += 1
                if match == len(counter):
                    while index and counter[s[index[0]]] <= 0:
                        if i-index[0] < ans[1]-ans[0]:
                            ans[0], ans[1] = index[0], i
                        counter[s[index[0]]] += 1
                        if counter[s[index[0]]] > 0:
                            match -= 1
                            del index[0]
                            break
                        del index[0]
        if ans[1] == len(s):
            return ''
        return s[ans[0]:ans[1]+1]
                