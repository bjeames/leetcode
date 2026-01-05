class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preReqs[crs].append(prq)
        
        visiting = set()
        
        def dfs(c):
            if preReqs[c] == []:
                return True
            if c in visiting:
                return False

            visiting.add(c)
            for prq in preReqs[c]:
                if not dfs(prq):
                    return False
            visiting.remove(c)
            preReqs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

            
            




        