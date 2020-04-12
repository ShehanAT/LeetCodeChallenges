class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        testDict = []
        commonWord = ""
        if len(strs) == 0:
            return commonWord
        if len(strs) == 1:
            return strs[0]
        firstWord = strs[0]
        minLength = len(strs[0])
        commonIndex = 0
        for i in strs:
            if len(i) < minLength:
                minLength = len(i)   
        while(index < minLength):
            commonFlag = True
            for word in range(0, len(strs)):
                if firstWord[index] != strs[word][index]:
                    commonFlag = False
            if commonFlag == True:
                commonWord += firstWord[index]
                commonIndex = index
            index += 1
        print(commonWord)
        if len(commonWord) == 1 and len(firstWord) > 1 and commonIndex != 0:
            return ""
        else:
            return commonWord