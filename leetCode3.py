class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def buildChar(charCount):
            totalCount = 0
            for i in range(26):
                if charCount[i]:
                    totalCount += 1
                    charCount[i] -= 1
                    totalCount += buildChar(charCount)
                    charCount[i] += 1
            return totalCount
        charCount = [0] * 26
        for ch in tiles:
            charCount[ord(ch) - ord('A')] += 1
        return buildChar(charCount)