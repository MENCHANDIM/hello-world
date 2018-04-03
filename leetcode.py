class Solution(object):
    def twoSum(self, nums, target):

        # waiting list    
        potentialNumbers = {}
        
        index = 0
        
        for num in nums:
            
            # check if current number is less than targezt, if yes 
            if num <= target:
                
                # check if it's been expected, if no
                if not checkPresence(num, potentialNumbers):
                    
                    # and store index
                    potentialNumbers[target - num] = index
                    
                else :
                    index1 = potentialNumbers.get(num)
                    index2 = index
                    return [index1, index2]
            index = index + 1
                    
def checkPresence(num, group):
    for key, value in group.items():
        if num == key:
            return True
    return False
        
                      
solution = Solution()
nums = [0,4,3,0]
target = 0

print(solution.twoSum(nums, target))
