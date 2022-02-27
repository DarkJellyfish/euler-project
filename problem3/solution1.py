factor_number = 600851475143

i = 2
while i * i <= factor_number:
    if factor_number % i:
        i += 1
    else:
        factor_number //= i

print(factor_number)
