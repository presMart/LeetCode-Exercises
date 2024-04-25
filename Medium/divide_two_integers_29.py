class Solution:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        q_sign = "-" if ((dividend < 0) ^ (divisor < 0)) else ""

        dend = abs(dividend)
        dor = abs(divisor)
        q = 0
        while dend - dor >= 0:
            x = 0
            while dend - (dor << 1 << x) >= 0: # while dividend minus (divisor bit shifted left once, divisor bit shifted x times) is greater than or equal to 0
                x += 1 # while the above is True, increment x by 1, and check if divisor can still go into dividend after being left shifted (x) times
            q += 1 << x # increment q by the number of times we can double the divisor while it can still fit into dividend
            dend -= dor << x # decrement dividend by how many times divisor was doubled (ie, by how many times dor was shifted left)

        cleaned_q = int(f'{q_sign}{q}')
        if cleaned_q >= 2147483647:
            return 2147483647
        elif cleaned_q <= -2147483648:
            return -2147483648
        return cleaned_q

