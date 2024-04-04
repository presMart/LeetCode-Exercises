class Solution:
    # def numberOfSteps(self, num: int) -> int:
    #     steps = 0
    #     result = None
    #     while result is None:
    #         # Use similar approach as mapped solution to fizz_buzz

    # def numberOfSteps(self, num: int) -> int:
    #     steps = 0
    #     while num > 0:
    #         if num % 2 == 0:
    #             num //= 2
    #         else:
    #             num -= 1
    #         steps += 1
    #     return steps

    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

    def explainedBitwiseNumberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        bin_num = bin(num)[2:]
        # The easier to read version:
        steps = 0

        for bit in bin_num:
            # Must use "1", not 1 here. The bits are strings!
            if bit == "1":  # If the bit is a 1
                steps = steps + 2  # Then it'll take 2 to remove.
            else:  # bit == "0"
                steps = steps + 1  # Then it'll take 1 to remove.

            # We need to subtract 1, because the last bit was over-counted.
        return steps - 1

    def cleanedBitwiseNumberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        bin_num = bin(num)[2:]
        ones = bin_num.count('1')
        total = len(bin_num)
        return ones + total - 1

