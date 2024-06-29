n = 11
my_set = set()
sum = 0
nums = n

#while digits of nums is greater than 2
while (len(str(nums)) > 1):
    sum = (n%10) * (n%10) + sum
    n = n // 10

    if n == 0:
        if sum == 1:
            print("yipee")
        n = sum
        nums = n
        sum = 0
        my_set.add(n)
    
    elif n in my_set:
        print("Womp womp")

if n == 1:
    print("yes")
else:
    print("no")

