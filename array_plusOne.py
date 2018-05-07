class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rem = 1
        length = len(digits)-1

        for count, digit in enumerate(reversed(digits)):
            digits[length-count] = (digit + rem) % 10
            rem = (digit + rem) // 10

        if rem == 1:
            return [1] + digits
        else:
            return digits


# #best solution
# class Solution:
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         carry = 1
#         for i in range(len(digits)-1, -1, -1):
#             digits[i] += carry
#             if digits[i] > 9:
#                 digits[i] -= 10
#                 carry = 1
#             else:
#                 carry = 0
#             if carry == 0:
#                 break
#         if carry == 1:
#             digits.insert(0, 1)
#         return digits
