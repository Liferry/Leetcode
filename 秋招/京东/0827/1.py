class Solution:
    def __init__(self):
        self.elements = ["2", "3", "5"]

    def func(self, n):
        """
        Args:
            n: int
        
        Return:
            str
        """
        if n < 3:
            return self.elements[n]

        n
        i = 1
        while n >= 3 ** i:
            n -= 3 ** i
            i += 1
        
        shan, yushu = divmod(n, 3 ** (i - 1))
        res = self.elements[shan]
        other = self.func(yushu + (3 ** (i - 2) if i - 2 > 0 else 0))
        return res + other


if __name__ == "__main__":
    # n = int(input())
    n = 12
    print(Solution().func(n - 1))