class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        ans=''
        for i,num in enumerate(nums):
            
            ans+= '1' if(num[i]=='0') else '0'    
        return ans