list1 = []
list2 = [1,3,18,21,24]
final1 = []
p1=p2=0

while (p1 < len(list1) and p2 < len(list2)):
    if list1[p1] == list2[p2]:
        final1.append(list1[p1])
        final1.append(list2[p2])
        p1 += 1
        p2 += 1
        
    elif list1[p1] > list2[p2]:
        final1.append(list2[p2])
        p2 +=1
    else:
        final1.append(list1[p1])
        p1 +=1

if len(list1[p1:]) > len(list1[p2:]):
    final1.extend(list1[p1:])
else:
    final1.extend(list2[p2:])
print(final1)
