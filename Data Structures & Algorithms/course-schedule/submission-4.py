class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adj_list = { i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            
            adj_list[course].append(prereq)
        
        visited = set()

        def dfs(course):
            
            if course in visited: return False # Detected a Cycle

            if adj_list[course] == []: return True # Course Can be Taken.  

            visited.add(course) # Add to seen list -> Going to call DFS on all Nodes.

            for pre_req in adj_list[course]:

                if not dfs(pre_req): return False

            visited.remove(course) # Done Processing this Node and all edges.

            adj_list[course] == [] # Set to Empty list to reduce reprocessing.

            return True

        for courses in range(numCourses):
            if not dfs(courses):
                if not dfs(courses): return False 
        return True 

        