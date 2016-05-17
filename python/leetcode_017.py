class Solution(object):
    def letterCombinations(self,digits):
        """
        :type digits:str
        :rtype:List[str]
        """
        ans=[]
        map={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits)==0:
            return ans
        if len(digits)==1:
            return list(map[digits[0]])
        else:
            result=self.letterCombinations(digits[1:])
            for i in map[digits[0]]:
                for j in result:   
                    ans.append(i+j)
        return ans
if __name__=="__main__":
    digits="378"
    x=Solution()
    ans=x.letterCombinations(digits)
    print ans
