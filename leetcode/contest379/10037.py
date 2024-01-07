class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        remove = len(nums1) / 2
        
        set1 = set(nums1)
        set2 = set(nums2)
        n = len(nums1) - len(set1)
        if n < remove:
            for item in (set1 & set2):
                n += 1
                set1.remove(item)
                if n >= remove:
                    break
        if n < remove:
            tempSet = set()
            for item in set1:
                n += 1
                tempSet.add(item)
                if n >= remove:
                    break
            set1 -= tempSet
        n = len(nums2) - len(set2)            
        if n < remove:
            for item in (set1 & set2):
                n += 1
                set2.remove(item)
                if n >= remove:
                    break
        if n < remove:
            tempSet = set()
            for item in set2:
                n += 1
                tempSet.add(item)
                if n >= remove:
                    break
            set2 -= tempSet
        return len(set1 | set2)
