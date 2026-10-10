class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        anagram = False

        sDic = self.countLetters(s)
        tDic = self.countLetters(t)
        if sDic == tDic:
            anagram = True
        else:
            anagram = False 

        return anagram


    def countLetters(self, word: str) -> List:
        wordDic = {}
        wordLen = len(word)
        for n in word:
            if n in wordDic:
                wordDic[n] += 1
            else:
                wordDic[n] = 1 
        return wordDic

obj1 = Solution()
obj1.countLetters("word")