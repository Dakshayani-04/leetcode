class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count= {}
        for ch in t:
            count[ch]=count.get(ch,0)+1
        for ch in s:
            count[ch] -= 1
        for ch in count :
            if count[ch]== 1:
               return ch
        