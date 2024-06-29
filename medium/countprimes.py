n = 25
l2 = []
# l1 = [True] * n
# l1[0] = l1[1] = False

# for prime in range(2,1+int(n ** 0.5)):
#     for num in range(prime * prime, n, prime):
#         l1[num] = False

for i in range(2,n):
    l2.append(i)

for prime in range(2,1+int(n ** 0.5)):
    if prime in l2:
        for num in range(prime * prime, n, prime):
            l2.remove(num)

print(len(l2))