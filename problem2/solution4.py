first, second, even_sum = 0, 1, 0

while first < 4000000:
    if first % 2 == 0:
        even_sum += first
    a, b = b, a + b

print(even_sum)
