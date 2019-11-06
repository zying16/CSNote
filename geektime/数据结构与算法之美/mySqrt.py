class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left = 1
        right = x // 2
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left
