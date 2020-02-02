'''
10개의 정수를 입력 받아 부분집합의 합이 0이 되는 부분집합이 몇개인지
계산하는 함수를 작성해보자.
'''
def powerset(arr):
    cnt = 0
    for i in range(1, 1 << len(arr)):
        sum = 0
        for j in range(len(arr)):
            if i & (1 << j): sum += arr[j]

        if sum == 0:
            # for j in range(len(arr)):
            #     if i & (1 << j):
            #         print(arr[j], end= " ")
            # print()
            cnt += 1
    return cnt

arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# arr = list(map(int, input().split()))
print(powerset(arr))