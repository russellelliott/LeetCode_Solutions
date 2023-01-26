class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*(len(s)+1) #initalize array of zeros
        # length 0 string has 0 flips
        #array is length of string + 1
        count = 0 #number of zeros
        for i in range(1, len(s)+1): #i is length of string
            if s[i-1] == "1":
                #carry over count
                dp[i] = dp[i-1]
                count+=1 #increment count; saw 1
            else:
                #zero, 2 cases
                dp[i] = min(count, dp[i-1]+1)
                #left; flip all the ones before it
                #right; flip the zero
                #which is cheaper to do;
        
        return dp[-1]
            
        

#monotone in creaing; can be increasing or the same, but never decreasing

'''
try to flip one number; do this for all the numbers
if it's monotone increasing, stop
if still not monotone at the end, try flipping 2 at a time?
'''

#string length x, find all possible monotone increasing
#number of flips on strings to get that. find the one that is the least

#start from left to right
'''
go to first one. from ther, create tree
flip or keep
keep track of flips
'''

#solution: sliding window
'''
ex: 01101110010
count number of 0s and 1s
5 zeros, 6 1s
will result of strings of 0s or 1s. not idea

for now; 2 sections
end result: 2 sections
- 1 section full of zeros
- 1 section full of 1s
- find division for 0s and 1s
- comparte flips on either side
- increment left, decrement right
- icnrementing left, decrementing right; just adding one character; just increase a counter
- o(n) time to scan string
- full right: 1 full pass; o(n)
- do next for loop
'''

#solution 2: 
'''
0110111000
000001 11111

prefix is monotone increasing
next character
worry about each character we come across

0 is monotone increasing
1 monotne
1 yes
0 no
- make decision of that zero; flip
1 yes
1 yes
1 yes
0 no
- make decision; flip

'''


'''
2 cases
i is length of the string we are looking at
i = length of substring
go through list; how amny flips for previous flips
storage is dp

how many flips for empty string: 0
dp[0] = 0

given string s
for i>=1, if s[i-1] = "1" then dp[i] = dp[i-1]
for i>=1 if s[i-1] = "0"
2 subcases
- if don't flip the zero, we have to flip all the 1s before it
- if we do flip the zero, then dp[i]=dp[i-1]+1


seperate counter of number of 1's we've seen

dp is array

'''