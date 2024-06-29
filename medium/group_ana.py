hash_table = {}
strs = ["eat","tea","tan","ate","nat","bat"]
l1 = []
l2 = []

for i in strs:
    curr = ''.join(sorted(i))
    if curr in hash_table:
        hash_table[curr].append(i)
    else:
        hash_table[curr] = [i]


for key in hash_table:
    l2.append(hash_table[key])

print(l2)