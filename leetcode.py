# class Solution(object):
#     def twoSum(self, nums, target):

#         # waiting list    
#         potentialNumbers = {}
        
#         index = 0
        
#         for num in nums:
                
#             # check if it's been expected, if no
#             if not checkPresence(num, potentialNumbers):
                
#                 # and store index
#                 potentialNumbers[target - num] = index
                
#             else :
#                 index1 = potentialNumbers.get(num)
#                 index2 = index
#                 return [index1, index2]
#             index = index + 1
                    

# def checkPresence(num, group):
#     for key, value in group.items():
#         if num == key:
#             return True
#     return False
        

# def main():

#     solution = Solution()
#     nums = [-3,4,3,90]
#     target = 87
#     print(solution.twoSum(nums, target))


class Solution(object):
    def twoSum(self, nums, target):

        length = len(nums)
        
        for i in range(0, length):
            for j in range(i+1, length):
                if target == nums[i] + nums[j]:
                    return [i,j]

def main():
    solution = Solution()
    nums = [899,4,3,90]
    target = 903
    print(solution.twoSum(nums, target))


if __name__ == '__main__':
    main()
