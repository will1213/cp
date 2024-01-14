class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        words = defaultdict(list)
        for word in wordList:
            for i in range(n):
                words[word[:i] + '*' + word[i+1:]].append(word)
        ans = math.inf
        q = [[beginWord, 1]]
        used = set()
        used.add(beginWord)
        while q:
            temp = q.pop(0)
            word = temp[0]
            level = temp[1]
            for i in range(n):
                myString = word[:i] + '*' + word[i+1:]
                if endWord in words[myString]:
                    ans = min(ans, level+1)
                else:
                    for w in words[myString]:
                        if w not in used:
                            q.append([w, level+1])
                            used.add(w)
        if ans == math.inf:
            return 0
        return ans
