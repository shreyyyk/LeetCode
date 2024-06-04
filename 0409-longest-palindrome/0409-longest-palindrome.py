class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=set()
        res=0
        for letter in s:
            if letter in count:
                res+=2
                count.remove(letter)
            else:
                count.add(letter)
        if count:
            return res+1
        else:
            return res