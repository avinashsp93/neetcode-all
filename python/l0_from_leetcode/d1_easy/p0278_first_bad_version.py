class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        isBad = False
        badVersion = 0
        while(left <= right):
            mid = (left + right) // 2

            isBad = isBadVersion(mid)

            if isBad:
                badVersion = mid
                right = mid - 1
            else:
                left = mid + 1

        return badVersion
    
def isBadVersion(version: int):
    bad = 10 # mock value
    return version >= bad