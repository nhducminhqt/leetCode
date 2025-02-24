from collections import defaultdict

class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        time_bob = {bob: 0}  
        def dfs_bob(node, parent, time):
            if node == 0:
                return True  
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    time_bob[neighbor] = time + 1
                    if dfs_bob(neighbor, node, time + 1):
                        return True
            
            del time_bob[node] 
            return False

        dfs_bob(bob, -1, 0)  
        max_profit = [float('-inf')]  

        def dfs_alice(node, parent, time, profit):
            if node in time_bob:
                if time < time_bob[node]:  
                    profit += amount[node]
                elif time == time_bob[node]:  
                    profit += amount[node] // 2
            else:
                profit += amount[node]  
            
            if len(graph[node]) == 1 and node != 0:
                max_profit[0] = max(max_profit[0], profit)
                return
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs_alice(neighbor, node, time + 1, profit)

        dfs_alice(0, -1, 0, 0)  

        return max_profit[0]  