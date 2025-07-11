class Solution:
    def reverse(self, x: int) -> int:
        input_num = x
        x = abs(x)
        reverse = 0

        while -2**31 < reverse < 2**31 - 1:
            if x == 0:
                if input_num < 0:
                    return reverse * -1
                else:
                    return reverse
            
            reverse = reverse * 10 + (x % 10)
            x //= 10
        
        return 0
        
