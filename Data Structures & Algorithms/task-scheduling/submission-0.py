class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)

        for task in tasks: # n
            count[task] += 1
        
        heap = [] # max queue
        for task, freq in count.items(): # m: number of unique tasks (max 26)
            # frequency, task
            # want to do the most frequent one first to let it cooldown first
            heap.append((-freq, task))
        heapq.heapify(heap) # m

        time = 0
        cooldown = []
        while heap or cooldown:
            if not heap: # max queue is empty so we skip ahead
                cd, freq, task = cooldown.pop(0)
                time = cd
            else:
                freq, task = heapq.heappop(heap)
            freq += 1

            time += 1
            if freq != 0:
                cooldown.append((time+n, freq, task))
            
            # process all cooldowns that can go back to queue
            while cooldown and cooldown[0][0] <= time:
                _, freq_cd, task_cd = cooldown.pop(0)
                heapq.heappush(heap, (freq_cd, task_cd))

        return time