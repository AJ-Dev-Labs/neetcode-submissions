class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        lowS = s.lower()

        for c in lowS:
            dig = ord(c)
            if((dig >= 97 and dig <= 122) or (dig >=48 and dig <= 57)):
                strs = strs+c

        left = 0
        right = len(strs) - 1

        while(left < right):
            if(strs[left] != strs[right]):
                return False
            else:
                left +=1
                right -=1
        return True

        