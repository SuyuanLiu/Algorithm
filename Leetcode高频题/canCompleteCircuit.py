'''
@lsy 2019.11.29

如果 sum_gas < sum_cost，一定无法完成目标；否则一定有解；
如果从 A 出发，无法到达 B，那么从这中间的任何一点出发都不能满足条件。
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas, sum_cost = 0, 0
        start = 0
        tank = 0
        
        for i in range(len(gas)):
            sum_gas, sum_cost = sum_gas + gas[i], sum_cost + cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        if sum_gas < sum_cost:
            return -1
        return start
