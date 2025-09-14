import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

'''
- Q1. ✍️ 농심 라면 공장
    ❓ Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
    해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
    현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
    dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30

# 다음과 같이 입력값이 들어온다면,
# 현재 재고가 4개 있습니다. 그리고 정상적으로 돌아오는 날은 30일까지입니다.
# 즉, 26개의 공급량을 사와야 합니다!
# 그러면 제일 최소한으로 26개를 가져오려면? supplies 에서 20, 10 을 가져오면 되겠죠?
# 그래서 이 경우의 최소 공급 횟수는 2 입니다!

stock = 0
dates = [0, 10, 15]
supplies = [20, 10, 15]
k = 35

# 이 때! 다음과 같이 입력값이 들어온다면 어떻게 해야 할까요?
# supplies 에서 20, 15를 가져오는게 가장 최고의 상황입니다!
# 즉, 0일과 15일에 공급량을 가져오는 게 좋습니다!

stock = 0
dates = [0, 20, 25]
supplies = [20, 10, 15]
k = 35

# 이 때! 다음과 같이 입력값이 들어온다면 어떻게 해야 할까요?
# supplies 에서 20, 10, 15를 가져와야만 합니다.
# 공장이 멈추지 않기 위해서는, 밀가루가 떨어지기 전에 
# 가져올 수 있는 밀가루를 전부 보충해야 하니까요!
# 즉, 현재 재고가 바닥나는 시점 이전까지 받을 수 있는 밀가루 중 
# 제일 많은 밀가루를 받는 게 목표입니다!
'''
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    count = 0
    heap = []
    dates.append(k)
    supplies.append(0)
    for i in range(len(dates)):
        while stock < dates[i]:
            if not heap:
                return -1
            max_supply = -heapq.heappop(heap)
            stock += max_supply
            count += 1
        heapq.heappush(heap, -supplies[i])
    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))  
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))