# Lesson Цикл for. Элементы списка. Полезные функции в цикле

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
n = (len(numbers))
for i in range(n):
    k = 0
#    print(numbers[i])
    for j in range(1, numbers[i]):
        if (numbers[i] % j == 0):
            k += 1
    if k <= 2:
        primes.extend([numbers[i]])
    else:
        not_primes.extend([numbers[i]])
print('numbers = ',numbers)
print('Primes = ', primes)
print('Not_primes = ', not_primes)
