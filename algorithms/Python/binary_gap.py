"""
? Вам дано число n, для которого необходимо найти самое длинное расстояние между единицами в двоичной форме записи числа
! На вход подаётся одно число n = 22
* Необходимо вернуть расстояние между двумя единицами. Расстояние должно быть максимальным, и расстоянием считается только
промежуток между двумя единицами разделенными нулями. К примеру 1001 - расстояние 3, а 10110 рассстояние будет расчитываться
между 101 но не между 1011.
Пример:
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
"""

n = 22

def binary_gap(n):
        A = [i for i in xrange(32) if (n >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in xrange(len(A) - 1))

print(binary_gap(n))