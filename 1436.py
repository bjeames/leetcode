class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # create dictionary (graph)
        graph = {}
        for segment in paths:
            graph[segment[0]] = segment[1]
        # iterate over each pair in path, and do graph.get(pair[0])
        for segment in paths:
            # if none, return destination
            if graph.get(segment[1]) == None:
                return segment[1]