class Solution:
    def fib(self, n: int) -> int:
        one, two = 0, 1

        for i in range(n):
            one, two = two + one, one

        return one