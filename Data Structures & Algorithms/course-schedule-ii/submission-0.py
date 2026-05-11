class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = { courses:[] for courses in range(numCourses) }

        for course, pre_req in prerequisites:

            adj_list[course].append(pre_req) # Map Course -> List of Pre-Reqs

        output = []

        visited, cycle = set(), set()

        def dfs(course):
            
            if course in cycle: return False # Detected a Cycle

            if course in visited: return True # Node has been already processed.

            cycle.add(course)

            for pre_req in adj_list[course]:

                if not dfs(pre_req): return False

            cycle.remove(course) # After we go through all the edges -> Done Processing Remove

            visited.add(course) # Now mark this course as visited.

            output.append(course)

            return True 
    
        for course in range(numCourses):
            
            if dfs(course) == False: 
                return [] 
        
        return output



                






            