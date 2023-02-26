class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        msa = k
        left = 0
        freq_map = {}
        max_frequency = 0
        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            
            max_frequency = max(max_frequency, freq_map[s[right]])
            
            if right - left + 1 > max_frequency + k:
                freq_map[s[left]] -= 1
                left += 1
                
                
            msa = max(right-left + 1, msa)
        return msa