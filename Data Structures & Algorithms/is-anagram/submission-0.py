class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if m!=n:
            return False
        else:
            c = [0]*26

            for i in range(n):
                a = ord(s[i]) - 97
                b = ord(t[i]) - 97
                c[a] = c[a] + 1
                c[b] = c[b] - 1
            
            for i in c:
                if i != 0:
                    return False
            return True


        