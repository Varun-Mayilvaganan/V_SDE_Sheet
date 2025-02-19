class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        
        s1_counts = [0]*26
        s2_counts = [0]*26
        for i in range(l1):
            s1_counts[ord(s1[i])- 97] += 1
            s2_counts[ord(s2[i])- 97] += 1
        if s1_counts == s2_counts:
            return True
        
        for j in range(l1, l2):
            s2_counts[ord(s2[j]) - 97] += 1
            s2_counts[ord(s2[j - l1]) - 97] -= 1
            if s1_counts == s2_counts:
                return True
        return False

        
