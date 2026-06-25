class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in s:
                if s.count(i) == t.count(i):
                    b =  True
                else:
                    b =  False
                    break
            return b
        else:
            return False
        