class Solution:

    def kthElement(self, a, b, k):
        def merge_arr(a,b):
            i, j = 0, 0
            merged = []
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1
            merged.extend(a[i:])
            merged.extend(b[j:])
            
            return merged
        
        # just return the kth position value
        sorted_list = merge_arr(a,b)
        return sorted_list[k-1] 
