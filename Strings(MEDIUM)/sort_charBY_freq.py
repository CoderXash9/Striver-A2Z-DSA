class Solution:
    def frequencySort(self, s):
        freq = {}

        # Count frequency of each character
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Sort by:
        # 1. Frequency (descending)
        # 2. Character (ascending)
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Store only the characters
        ans = []

        for char, count in sorted_chars:
            ans.append(char)

        return ans
