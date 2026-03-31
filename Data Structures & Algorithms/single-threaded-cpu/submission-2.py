class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Use a min heap
        heap = []
        res = []

        for i in range(len(tasks)):
            tasks[i] = [tasks[i][0], tasks[i][1], i]

        # sort by enque time
        # O(nlog(n))
        tasks.sort(key=lambda x: x[0])
        
        heapq.heappush(heap, (tasks[0][1], tasks[0][2], tasks[0][0]))
        index = 1
        time = tasks[0][0]
        while heap or index < len(tasks):
            # Add the new enqueues that occured in the processing of the above task
            while index < len(tasks) and tasks[index][0] <= time:
                heapq.heappush(heap, (tasks[index][1], tasks[index][2], tasks[index][0]))
                index += 1
            
            if not heap:
                time = tasks[index][0]
            else:
                process, i, enqueue = heapq.heappop(heap)
                time = max(enqueue, time) + process
                res.append(i)
        return res