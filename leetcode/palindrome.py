class Solution:

    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes (e.g., -121 reversed is 121-)
        if x < 0:
            return False

        # Store the original value of x because x will become 0 during the loop
        original_x = x
        reversed_x = 0

        # Your classic integer-reversing loop
        while x > 0:
            digit = x % 10
            reversed_x = (reversed_x * 10) + digit
            x //= 10

        # Check if the reversed number is identical to the original number
        return reversed_x == original_x