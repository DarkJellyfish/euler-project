fib_sum = 2

first = 1
second = 2

while (second < 4000000):
    new_term = first + second
    if (new_term % 2 == 0):
        fib_sum += new_term

    # reset the terms
    first = second
    second = new_term

print(fib_sum)
