class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build the graph
        graph = defaultdict(list)
        price_chart = {}
        cache = {}
        for src_i, dst_i, price in flights:
            graph[src_i].append(dst_i)
            price_chart[(src_i, dst_i)] = price
        
        def find_cheapest(airport, stops, total):
            if airport == dst:
                return total
            if stops > k:
                return float("inf")

            local_price = float("inf")
            for next_airport in graph[airport]:
                if (airport, next_airport, stops+1) not in cache:
                    cache[(airport, next_airport, stops+1)] = find_cheapest(next_airport, stops+1, total+price_chart[(airport, next_airport)])
                local_price = min(local_price, cache[(airport, next_airport, stops+1)])

            return local_price

        res = float("inf")
        for dest in graph[src]:
            calc_price = find_cheapest(dest, 1, price_chart[(src, dest)])
            res = min(res, calc_price)

        return res if res != float("inf") else -1
