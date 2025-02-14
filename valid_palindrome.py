class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res = res + i
        res = res.lower()
        if res == res[::-1]:
            return True     
