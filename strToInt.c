import re 
class Solution:
    def myAtoi(self, str: str) -> int:
        try:
            newStr1 = str.split()[0]
        except:
            newStr1 = str.split()
        if "+-" in newStr1:
            return 0
        if len(newStr1) == 0:
            return 0 
        newStr2 = newStr1.split(".")[0]
        newStr2 = newStr2.split("+")
        if newStr2[0] == "" and len(newStr2) > 1:
            print(newStr2)
            newStr2 = newStr2[1]
        else:
            newStr2 = newStr2[0]
        
        newStr3 = re.split("[^\W\d_]+", newStr2)[0]
        
        try:
            
            if newStr3[len(newStr3) - 1] == "-":                
                return int(newStr3[:-1])
            if int(newStr3) > 2147483647:
                return 2147483647
            if int(newStr3) < -2147483648:
                return -2147483648
            else:
            
                return int(newStr3)
        except:
            return 0
    
