class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix (str1, str2):
            l = len(str1)
            l2 = len(str2)
            if l > l2:
                return False
            if str2[:l] == str1 and str2[l2-l:] == str1:
                return True
        wordLen = len(words)
        ans = 0
        for i in range(wordLen):
            for j in range(i+1, wordLen):
                if isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans
            
                