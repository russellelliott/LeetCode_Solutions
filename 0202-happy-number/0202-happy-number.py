class Solution(object):
    def testLoop(self, n):

        digits_string = str(n)
        digits = []
        for digit in digits_string:
            digits.append(digit)
        
        print(digits)

        square_sum = 0
        for digit in digits:
            digit_int = int(digit)
            square_sum+=digit_int**2
        
        print(square_sum)

        return square_sum
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        

        # 1. split n into digits
        # 2. square
        # 3. sum sqaures into new number
        # 4. repeat step 1 loop

        #detecting a cycle?
        # case where cycle?
        # - check if cycle, numbers
        # list could be sufficient, but something more optimized for search
        #dictionary could work? search by keys
        #dictionary with just keys (extra memory)
        #set (unique list)
        #know it'll be 1; check if digits sum to one


        current_number = n
        numbers_set = set()
        while(current_number!=1):
            current_number = self.testLoop(current_number)
            print(current_number)
            if(current_number in numbers_set):
                return False
            numbers_set.add(current_number)
        
        return True