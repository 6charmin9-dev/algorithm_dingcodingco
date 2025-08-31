array = [5, 3, 2, 1, 6, 8, 7, 4]

# MergeSort(0, N) = Merge(MergeSort(0, N/2), MergeSort(N/2, N))
def merge_sort(array):
    # 이 곳을 채워보세요!
    if len(array) <= 1:
        return array
    mid = len(array)//2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

def merge(array1, array2):
    result = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    while i < len(array1):
        result.append(array1[i])
        i += 1
    while j < len(array2):
        result.append(array2[j])
        j += 1
    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))

# 시간복잡도: O(N log N) : N 만큼의 연산을 log N 번 수행