class Solution:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        dend_mag = False if dividend < 0 else True
        dor_mag = False if divisor < 0 else True
        neg = True if (dend_mag and not dor_mag) or (not dend_mag and dor_mag) else False
        x = abs(dividend) - abs(divisor)
        t = 1 if x == 0 else 0
        if x > 0:
            abs_dor = abs(divisor)
            while x > 0:
                x -= abs_dor
                t += 1
        return t if not neg else -abs(t)

    def divide2(self, dividend: int, divisor: int) -> int:
        dend_mag = False if dividend < 0 else True
        dor_mag = False if divisor < 0 else True
        neg = True if (dend_mag and not dor_mag) or (not dend_mag and dor_mag) else False
        x = abs(dividend) - abs(divisor)
        t = 1 if x == 0 else 0
        if x > 0:
            abs_dor = abs(divisor)
            while x > 0:
                x -= abs_dor
                t += 1
        return t if not neg else -abs(t)

    def div_alt(self, dividend: int, divisor: int) -> int:
        dend_mag = False if dividend < 0 else True
        dor_mag = False if divisor < 0 else True

        x = abs(dividend) - abs(divisor)
        t = 1
        if x > 0:
            while x >= 0:
                x -= divisor
                t += 1
        if (dend_mag and not dor_mag) or (not dend_mag and dor_mag):
            return -abs(t-1)
        return t - 1


    def divide_unsigned(self, dividend: int, divisor: int):
        q = 0
        r = dividend

        while r >= divisor:
            q += 1
            r -= divisor

        return q, r

    def divideAlt(self, dividend: int, divisor: int) -> int:

        if divisor < 0:
            q, r = self.divideAlt(dividend, -abs(divisor))
            return -abs(q)

        if dividend < 0:
            q, r = self.divideAlt(-abs(dividend), divisor)
            if r == 0:
                return -abs(q)
            else:
                return -abs(q) - 1
        q,r = self.divide_unsigned(dividend, divisor)

        # if divisor < 0:
        #     print(d(dividend, abs(divisor)))
        #     q, r = d(dividend, abs(divisor))
        #     return -abs(q)
        # if dividend < 0:
        #     q, r = d(abs(dividend), divisor)
        #     if r == 0:
        #         return -abs(q)
        #     else:
        #         return -abs(q) - 1
        # return divide_unsigned(dividend, divisor)


    #     return self.divide_unsigned(dividend, divisor)


def d(dividend, divisor):
    if divisor < 0:
        print("----   1")
        print(d(dividend, abs(divisor)))
        q, r = d(dividend, abs(divisor))
        print(q)
        return -abs(q), r
    if dividend < 0:
        print("----   2")
        q, r = d(abs(dividend), divisor)
        print(q)
        if r == 0:
            print("----   3")
            return -abs(q), 0
        else:
            print("----   4")
            return -abs(q) - 1, divisor - r
    print("----   5")
    return divide_unsigned(dividend, divisor)