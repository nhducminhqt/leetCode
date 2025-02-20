class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def helper(path):
            nonlocal res, letters
            if len(path) == n:
                res += [path]
                return
            for ch in letters:
                if len(path) > 0 and path[-1] == ch:
                    continue
                helper( path + ch)
        letters = ['a', 'b', 'c']
        res = []
        helper('')
        if len(res) < k:
            return ''
        res = sorted(res)