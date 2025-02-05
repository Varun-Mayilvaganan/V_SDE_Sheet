class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
    
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
        
        # If there are exactly two differences, check if they can be swapped
        if len(diff_indices) == 2:
            i, j = diff_indices
            # Check if swapping s1[i] and s1[j] or s2[i] and s2[j] makes the strings equal
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # If there are no or more than two differences, return False
        return False
