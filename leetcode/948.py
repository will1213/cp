class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        tokens.sort()
        score = 0
        maxLen = len(tokens) - 1
        l = 0
        r = maxLen
        curScore = 0
        curPower = power
        while True:
            if l <= maxLen and tokens[l] <= curPower and l <= r:
                curPower -= tokens[l]
                curScore += 1
                l += 1
                score = max(score, curScore)
            else:
                if l > r or curScore == 0:
                    break
                else:
                    curPower += tokens[r]
                    curScore -= 1
                    r -= 1
        return score

