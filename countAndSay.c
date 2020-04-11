class Solution:
    def countAndSay(self, n: int) -> str:
        charPointer = 0
        counterPointer = 0
        frequencyPointer = 0
        finalStr = "1"
        progressStr = ""
        if n <= 0:
            return ""
        while(n > 1):
            n -= 1
            counterPointer = 0
            freqencyPointer = 0
            while(counterPointer < len(finalStr)):
                charPointer = finalStr[counterPointer]
                frequencyPointer = 0
                try:
                    while(finalStr[counterPointer] == charPointer):
                            counterPointer += 1
                            frequencyPointer += 1
                    raise ValueError
                except:
                    progressStr += str(frequencyPointer) + str(charPointer)
            finalStr = progressStr
            progressStr = ""
        return finalStr 
            