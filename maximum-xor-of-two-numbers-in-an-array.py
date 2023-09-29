def search_count(trie, bits):
    curr = trie
    count = 0
    length = 0
    for char in bits:
        if char == '0' and '1' in curr:
            count += 2**(32 - length-1)
            curr = curr['1']
        elif char == '1' and '0' in curr:
            count += 2**(32 - length-1)
            curr = curr['0']
        else:
            curr = curr[char]
        length += 1
    return count

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        bit_arr = []
        for i in range(len(nums)):
            bit_arr.append(format(nums[i], 'b'))
        trie = {}
        for i in range(len(bit_arr)):
            length = 32 - len(bit_arr[i])
            bit_arr[i] = '0'*length + bit_arr[i]
            curr = trie
            for bit in bit_arr[i]:
                if bit not in curr:
                    curr[bit] = {}
                curr = curr[bit]
        _max = 0

        for bits in bit_arr:
            length = 30 - len(bits)
            _max = max(_max, search_count(trie, '0' * length + bits))
        return _max