class Solution():
    def numDifferentIntegers( word):
        """
        :type word: str
        :rtype: int
        """
        current_num=""
        nums = []
        for letter in word:
            if(letter.isnumeric()):
                if letter =="0" and len(current_num)==0: continue
                current_num+= letter
            else:
                if current_num and not current_num in nums:
                    nums.append(current_num)
                current_num = ""
                    
      
        if current_num and not current_num in nums :nums.append(current_num)
        
        return len(nums) 




print(Solution.numDifferentIntegers("a123bc34d8ef34") == 3)
print(Solution.numDifferentIntegers("leet1234code234") == 2)
print(Solution.numDifferentIntegers("a1b01c001") == 1)
print(Solution.numDifferentIntegers("gi851a851q8510v") == 2)
