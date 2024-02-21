class Solution:
    def countAnagrams(self, s: str) -> int:
        ans = 1
        words = s.split(' ')
        for word in words:
            total = math.factorial(len(word))
            count = Counter(word)
            for v in count.values():
                total //= math.factorial(v)
            total = int(total) % (pow(10,9)+7)
            ans = (ans * total) % (pow(10,9)+7)
        return ans % (pow(10,9)+7)
            