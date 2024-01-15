class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        myDict = defaultdict(int)
        for match in matches:
            winners.add(match[0])
            losers.add(match[1])
            myDict[match[1]] += 1
        ans = [sorted(list(winners-losers))]
        temp = []
        for k,v in myDict.items():
            if v == 1:
                temp.append(k)
        ans.append(sorted(temp))
        return ans