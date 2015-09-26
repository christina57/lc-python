class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nextNum=n
        count=0
        while(nextNum!=1):
            nextNum=self.squareSum(nextNum)
            count+=1
            if(count==100):
                return False
        return True
        
    def squareSum(self, n):
        sqsum=0
        dividend=n
        while(dividend>0):
            sqsum+=pow(dividend%10,2)
            dividend/=10
        return sqsum