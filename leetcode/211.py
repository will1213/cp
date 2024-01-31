class WordDictionary:

    def __init__(self):
        self.myDict = defaultdict(dict)
        return

    def addWord(self, word: str) -> None:
        temp = self.myDict
        for c in word:
            if c not in temp:
                temp[c] = defaultdict(dict)
            temp = temp[c]
        temp['*'] = True
        return

    def mySearch(self, word, theDict):
        temp = theDict
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                myWord = word[i+1:]
                for v in temp.values():
                    if not isinstance(v, bool):
                        if self.mySearch(myWord, v):
                            return True
                return False
            elif c in temp:
                temp = temp[c]
            else:
                return False
        if '*' in temp:
            return True
        return False

    def search(self, word: str) -> bool:
        return self.mySearch(word, self.myDict)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)