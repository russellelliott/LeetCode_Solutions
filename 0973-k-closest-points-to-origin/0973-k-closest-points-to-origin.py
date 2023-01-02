class Solution(object):
    #distance of point to origin
    def distance(self, x, y):
        return sqrt(x**2 + y**2)
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        pointsList = [] #list to store points and distance
        for i in points:
            '''away = self.distance(i[0], i[1])
            pointsList[str(i)] = away'''
            #add pair
            away = self.distance(i[0], i[1])
            pointsList.append([i, away])
            
        #print(pointsList)
        
        #sort the list (do by 2nd item)
        #https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/
        sort = sorted(pointsList, key=lambda x:x[1])
        
        #get the first k items; the closest k points
        result = sort[0:k]
        #print(result)
        
        returnMe = []
        
        #the first item, the point, is what we want
        for i in result:
            returnMe.append(i[0])
        
        return returnMe