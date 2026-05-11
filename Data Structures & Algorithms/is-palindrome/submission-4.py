class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum()) #Change it to lowercase and make sure it
           #is all alphanumeric and then reverse the string and compare easy.
        return s == s[::-1]
        