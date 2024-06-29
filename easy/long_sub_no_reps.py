s = "pwwkew"
max_val = 0
max_list = []
letter_list = []
x = 0
        
s = list(s)

for i in range(len(s)-1):
    
    x = i + 1 
    
    while (s[x] != s[i]) & (s[x] not in letter_list):
        max_val = max_val + 1
        letter_list.append(s[x])
        if (x < len(s)-1):
            x = x + 1
        
            
    max_list.append(max_val)
    max_val = 0
    x = 0
    letter_list.clear()
print(max(max_list))


# for i in range(len(s)):
#     for x in range(1,len(s)):
#         if s[x] != s[i]:
            
#             max = max + 1
#         else:
#             break
            
#     inner_list.append(max)
#     max = 0

# print(max(inner_list))