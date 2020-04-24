class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # start = 0 # start range 
        # end = n # end range 
        # m = int(n/2) # start from the middle
        start, end, m = 0, n, int(n/2)  # this is equivalent to above 
        # n, int(n/2)
        while start <= end:
            curr = isBadVersion(m)
            prev = isBadVersion(m - 1)
            if prev == False and curr == True:
                return m
            elif prev == True and curr == True:
                end = m - 1 # narrowing the end 
                m = int((start + end) / 2)
            elif curr == False and prev == False:
                start = m + 1 # narrowing the start 
                m = int((start + end) / 2)