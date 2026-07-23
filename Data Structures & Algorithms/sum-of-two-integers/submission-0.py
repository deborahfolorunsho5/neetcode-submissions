class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

    # keep going while there's still a carry to add
        while b != 0:
        # find the carry: columns where BOTH bits are 1, shifted left one spot
            carry = (a & b) << 1
            a = (a ^ b) & mask

        # b becomes the carry, also trimmed to 32 bits, to add in on the next loop
            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)