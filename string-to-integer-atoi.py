class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        intString = ""
        digitF = 0
        signF = 0
        if len(s) == 0 :
            return 0
        for i in s :
            if i == ' ' and digitF==0 and signF == 0:
                continue
            elif i == '-' and digitF==0 and signF == 0:
                negative = True
                signF = 1
            elif i == '+'and digitF==0 and signF == 0:
                signF = 1
                continue
            elif i not in set("0123456789"):
                if digitF==0:
                    intString = "0"
                    break
                else :
                    break
            else :
                intString += i
                digitF = 1 
        
        uL = 2**31 - 1
        lL = - 2**31
        
        if negative == True and digitF!=0:
            t = int(intString)
            if -t < lL:
                return lL
            else :
                return -t
        
        elif negative == False and digitF!=0 :
            if int(intString) > uL :
                return uL
            else :
                return int(intString)
        
        return 0
