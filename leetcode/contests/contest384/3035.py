class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        count = defaultdict(int)
        for word in words:
            l = 0
            for c in word:
                l += 1
                count[c] += 1
        pairs = 0
        singles = 0
        for k, v in count.items():
            if v % 2 == 0:
                pairs += (v / 2)
            else:
                pairs += (v//2)
                singles += 1
        words.sort(key=lambda x: len(x))
        ans = 0
        for word in words:
            l = len(word)
            if pairs >= l // 2:
                pairs -= (l // 2)
                singles -= l % 2
                ans += 1
            else:
                break
        return ans