"""
? Вам дан массив, целых числел, необходимо заменить каждый элемент на его ранг среди всего массива.
! На вход подаётся массива вида: arr = [40,10,20,30]"
* Необходимо присвоить для кадого элемента его ранг относительно других элементов. Чем больше число, тем больше ранг. 
Для одинаковых чисел - одинаковый ранг. Ранги начинают своё отсчет с 1. Ранг должен стремиться быть как можно меньше.
Пример:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
"""

arr = [37,12,28,9,100,56,80,5,12]

def rank_assigning(arr):
    answer = set(sorted(arr, reverse=True))
        
    for i in range(0, len(arr)):
        rank_count = 1
        for item in answer:
            if arr[i] > item:
                rank_count += 1
        arr[i] = rank_count

    return arr

print(rank_assigning(arr))