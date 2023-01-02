class Solution(object):
    def distance(self, x1, x2, y1, y2):
        return abs(x1-x2)+abs(y1-y2)
    
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        
        #case 2
        '''default = [[x, y]]
        if(points == default):
            return 0'''
        
        #get the manhattan distance of all the points
        
        pointsList = [] #list to store points and distance
        for i in points:
            '''away = self.distance(i[0], i[1])
            pointsList[str(i)] = away'''
            #add pair
            away = self.distance(i[0], x, i[1], y)
            pointsList.append([i, away])
            
        #print(pointsList)
        
        #sort the list (do by 2nd item)
        #https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/
        sort = sorted(pointsList, key=lambda x:x[1])
        
        #append valid points
        '''for i in sort:
            if(i[0][0]==x and i[0][1]==y):
                valid.append(i[0])'''
        
        result = []
        #find the smallest distance
        default = sort[0][1]
        count = 0
        #loop until the distance changes. this gives us all the elements of the same distance
        #[[a, b], c]
        #i[0] = [a, b]
        #i[1] = c, the distance
        for i in sort:
            valid = i[0][0]==x or i[0][1] == y #point is valid if it shares the same x or y
            '''if(i[1] > default):
                break'''
            count+=1
            #result.append(i[0])
            if valid: #if the point is valid, add it to the list
                result.append(i[0])
        
        #case 3; no valid points
        if(len(result)==0):
            return -1
        
        #of points of the same distance, return the smallest index (where it is in list)
        #print(result)
        #return result
        searchFor = result[0]
        #print(searchFor)
        index=0
        for i in points: #go through all the points
            if i == searchFor: #we found the point
                break
            index+=1 #increment index until we find the shortest distance
        
        #print(index)
        return index
        

#reused: https://leetcode.com/problems/k-closest-points-to-origin/submissions/