class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # duplicated = False
        duplicated_dic = {} 
        for i in nums:
            if i in duplicated_dic:
                return True
            else:
                duplicated_dic[i] = i 
                print(i)
        return False

obj1 = Solution()
test = {4,5,6,7}
sol = obj1.hasDuplicate(nums = test)
        