class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            sLen = len(item)
            res = res + str(sLen)+"@"+item
        return res

    def decode(self, s: str) -> List[str]:
        temp = ""
        i = 0
        res = []
        while i < len(s):
            if(s[i] == "@"):
                sLen = int(temp)
                j = i+sLen+1
                word = s[i+1: j]
                res.append(word)
                temp=""
                i = j
            else:
                temp += s[i]
                i+=1
            
        return res


