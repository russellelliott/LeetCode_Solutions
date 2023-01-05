class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        words = [str(i) for i in words]
        
        for i in range(len(words)):
            if len(words[i])<=2:
                words[i] = words[i].lower()
            else:
                first = words[i][0].upper() #capitalize first
                remain = words[i][1:].lower() #lowercase the rest
                words[i] = first+remain #merge
        
        #print(words)
        
        result = " ".join(words) #join back into string
        return result