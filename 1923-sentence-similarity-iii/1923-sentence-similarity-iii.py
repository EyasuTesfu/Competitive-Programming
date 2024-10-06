class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # s1, let's consider we always add to sentence 1
        # where can we add it:
        # start A s1, es1 == es2, where e == end
        # middle ss1 A ss1 => ss1 == ss2 A= ms2 es1 == es2, one has extra field at the middle
        # end s1 A, => ss1 == ss2
        # if they're not similar at the star, then check their end, if that's not the same then it won't work.
        # if we have similarity and one length ends we return True
        # if we have similarity then difference we move while trying to 
        # similarity then difference could be dealt with 

        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        l1 = l2 = 0
        r1 = len(s1) - 1
        r2 = len(s2) - 1
        # not similar at the start
        if s1[l1] != s2[l2]:
            if s1[r1] != s2[r2]:
                return False
            min_length = min(len(s1), len(s2))
            # max_length = max(len(s1), len(s2))
            return s1[:min_length] == s2[len(s2)-min_length:] or s1[len(s1) - min_length:] == s2[:min_length]
        else:
            min_length = min(len(s1), len(s2))
            if s1[:min_length] == s2[:min_length]:
                return True
            else:
                while l1 <= r1 and l2 <= r2:
                    if s1[l1] != s2[l2]:
                        break
                    l1 += 1
                    l2 += 1
                if l1 > r1 or l2 > r2:
                    return True
                return s1[l1:] == s2[len(s2)-len(s1[l1:]):] or s2[l2:] == s1[len(s1) - len(s2[l2:]):]
        return False

            

