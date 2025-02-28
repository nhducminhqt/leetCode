class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table for LCS
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Step 2: Reconstruct the LCS
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        lcs = lcs[::-1]  # Reverse to get the correct order
    
    # Step 3: Construct the SCS
        scs = []
        i, j = 0, 0
        for char in lcs:
        # Add characters from str1 before the current LCS character
            while i < m and str1[i] != char:
                scs.append(str1[i])
                i += 1
        # Add characters from str2 before the current LCS character
            while j < n and str2[j] != char:
                scs.append(str2[j])
                j += 1
        # Add the LCS character
            scs.append(char)
            i += 1
            j += 1
    
    # Add remaining characters from str1 and str2
        while i < m:
            scs.append(str1[i])
            i += 1
        while j < n:
            scs.append(str2[j])
            j += 1
    
        return ''.join(scs)
        