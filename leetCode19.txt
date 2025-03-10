class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        is_vowel = {char: True for char in "aeiou"}  # Mark vowels
        freq = {}  # Dictionary to store character frequency
        
        response = 0
        current_k = 0
        vowel_count = 0
        extra_left = 0
        left = 0

        for right in range(len(word)):
            right_char = word[right]

            if right_char in is_vowel:
                freq[right_char] = freq.get(right_char, 0) + 1
                if freq[right_char] == 1:
                    vowel_count += 1
            else:
                current_k += 1

            # Shrink the window if consonant count exceeds k
            while current_k > k:
                left_char = word[left]
                if left_char in is_vowel:
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        vowel_count -= 1
                else:
                    current_k -= 1
                left += 1
                extra_left = 0

            # Adjust left pointer to remove extra vowels
            while vowel_count == 5 and current_k == k and left < right and word[left] in is_vowel and freq[word[left]] > 1:
                extra_left += 1
                freq[word[left]] -= 1
                left += 1

            # Count valid substrings
            if current_k == k and vowel_count == 5:
                response += (1 + extra_left)

        return response