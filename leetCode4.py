class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        num = 1
        res = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(num)
            num += 1
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    res.append(str(stack.pop()))

        return ''.join(res)
