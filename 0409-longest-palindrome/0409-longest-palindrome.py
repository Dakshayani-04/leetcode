class Solution:
    def longestPalindrome(self, s: str) -> int:
        count ={}
        for ch in s:
          count[ch]= count.get(ch,0)+1
        total =0
        odd =False
        for c in count.values():
            total += (c//2)*2
            if c % 2 == 1:
                odd=True
        if odd:
            total+= 1
        return total

        