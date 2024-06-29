flowerbed = [1,0,0,0,0,1]

flowerbed.append(0)
flowerbed.insert(0,0)
counted = 0


for flower in range(1,len(flowerbed)-1):
    if flowerbed[flower] == 0 and flowerbed[flower -1] == 0 and flowerbed[flower + 1] == 0:
        counted +=1
        flowerbed[flower] = 1
    else:
        continue

