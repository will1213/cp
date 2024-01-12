class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        count = 0
        for i in range(int(n/2)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                count += 1
        for i in range(int(n/2), n):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                count -= 1
        return count == 0