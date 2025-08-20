shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]
# shop_orders = ["오뎅", "콜라", "만두", "순대"]


'''
Q. 배달의 민족 서버 개발자로 입사했다.
상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
'''
def is_available_to_order2(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort() # 시간 복잡도: O(n log n)
    for order in orders:
        if not binary_search(menus, order):
            return False
    return True

def binary_search(arr, target):
    curr_min = 0
    curr_max = len(arr) - 1
    curr_guess = (curr_min + curr_max) // 2
    while curr_min <= curr_max:
        if arr[curr_guess] == target:
            return True
        elif arr[curr_guess] < target:
            curr_min = curr_guess + 1
        else:
            curr_max = curr_guess - 1
        curr_guess = (curr_min + curr_max) // 2
    return False

def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)