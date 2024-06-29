s = "Let's take LeetCode contest"
s = s.split()
l1 = "" + s[0][::-1]
for i in range(1,len(s)):
    l1 = l1 + " " + (s[i][::-1])
print(l1)