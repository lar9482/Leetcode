class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        children = {}
        inDegree = {}

        for edge in prerequisites:
            parent = edge[1]
            child = edge[0]

            if (children.get(parent) == None):
                children[parent] = [child]
            else:
                children[parent].append(child)

            if (inDegree.get(child) == None):
                inDegree[child] = 1
            else:
                inDegree[child] += 1
        
        queue = [nodeId for nodeId in range(0, numCourses) if inDegree.get(nodeId) == None]
        
        order = []
        while (len(queue) > 0):
            nodeId = queue.pop(0)
            order.append(nodeId)

            if (children.get(nodeId) != None):
                for childId in children[nodeId]:
                    inDegree[childId] -= 1

                    if (inDegree[childId] == 0):
                        queue.append(childId)

        if (numCourses == len(order)):
            return order
        else:
            return []