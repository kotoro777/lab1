#В массиве M(20) целых чисел подсчитать количество четных и нечетных чисел.
M = [10, 12, 5, 54, 21, 4, 45, 66, 93, 1, 31, 17, 7, 59, 3, 6, 47, 68, 22, 11]

even_count, odd_count = 0, 0

for num in M:

    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
