class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_array = sorted(list(s1))
        s2_array = []
        for right in range(len(s2)):
            s2_array.append(s2[right])
            if right - left + 1 == len(s1):
                if s1_array == sorted(s2_array[left:right+1]):
                    return True
                left += 1
        return False