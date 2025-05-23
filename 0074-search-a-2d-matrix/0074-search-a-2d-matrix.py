class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix[0]) - 1
        m1, m2 = 0, len(matrix)-1
        while m1 <= m2:
            m = (m1 + m2) // 2
            if matrix[m][0] <= target and matrix[m][n] >= target: #if target in range
                l, r = 0, n
                while l <= r:
                    mid = (l+r) // 2
                    if matrix[m][mid] > target:
                        r = mid - 1
                    elif matrix[m][mid] < target:
                        l = mid + 1
                    else:
                        return True
                return False
            elif matrix[m][0] > target: #first value too large
                m2 = m - 1
            elif matrix[m][n] < target: #last value too small
                m1 = m + 1
        return False
        