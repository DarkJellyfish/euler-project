limit = 4000000
num_list = []
a, b = 0, 1

for i in range(limit):
    if a < limit:
        num_list.append(a)
        a, b = b, a + b

print(sum(i for i in num_list if i % 2 == 0))
