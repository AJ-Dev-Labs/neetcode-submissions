class Solution:
    def isValid(self, s: str) -> bool:

        q = collections.deque()

        for c in s:
            if c == '(' or c == '[' or c == '{':
                q.append(c)
            else:
                if not q:
                    return False
                t = q[-1]
                if (c == ')' and t == '(') or (c == '}' and t == '{') or (c == ']' and t == '['):
                    q.pop()
                else:
                    return False
        return len(q) == 0