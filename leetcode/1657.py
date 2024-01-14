class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        if cnt1.keys() != cnt2.keys():
            return False
        cnt1 = Counter(cnt1.values())
        cnt2 = Counter(cnt2.values())
        return cnt1 == cnt2
        
