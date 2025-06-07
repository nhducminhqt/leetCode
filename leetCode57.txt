class Solution(object):
    def lexicalOrder(self, n):
        def g():
            c = 1
            for _ in range(n):
                yield c
                if c * 10 <= n:
                    c *= 10
                else:
                    while c % 10 == 9 or c + 1 > n:
                        c //= 10
                    c += 1
        return list(g())