
# LeetCode Problem 1672

class Solution:

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # This original attempt produced a better runtime than the alternative below
        w = 0
        for a in accounts:
            b = sum(a)
            if b > w:
                w = b
        return w

    def maximumWealthAlternative(self, accounts: List[List[int]]) -> int:
        # This alternative approach is more in line with the official answer on LC
        w = 0
        for a in accounts:
            w = max(w, sum(a))
        return w

    def maximumWealthOfficial(self, accounts: List[List[int]]) -> int:
        # The solution video has a good explanation of why this has a SPACE COMPLEXITY of O(1) - i.e. constant (in Java)

        # Initialize the maximum wealth seen so far to 0 (the minimum wealth possible)
        max_wealth_so_far = 0

        # Iterate over accounts
        for account in accounts:
            # Add the money in each bank
            curr_customer_wealth = sum(account)
            # Update the maximum wealth seen so far if the current wealth is greater
            # If it is less than the current sum
            max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)

        # Return the maximum wealth
        return max_wealth_so_far



