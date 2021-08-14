"""
? Вам дан массив "nums" длинны "n".
! На вход подаётся массив вида: nums = [2,2,1,1,1,2,2]
* Необходимо вернуть элемент, который является числом большинства. То есть вернуть нужно эллемент массива,
который встречается больше чем n/2 раз.
Пример:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
nums = [3,2,3]

def find_majority_el(arr):
        majority_count = len(arr)//2
        for num in arr:
            count = sum(1 for elem in arr if elem == num)
            if count > majority_count:
                return num

print(find_majority_el(nums))