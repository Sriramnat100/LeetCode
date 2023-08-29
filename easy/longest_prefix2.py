def longestCommonPrefix(strs):
        g = (strs[0])
        l1 = []
        f_l1 = []
        res = []
        max_count = 0
        final = ""
        empty = ""
        for i in strs:
            for x in range(len(strs)):
                if i[0] != g[0]:
                    return(empty)
                    break
                elif i[0:x] == g[0:x]:
                    l1.append(i[x])

        for i in l1:
            if l1.count(i) >= max_count:
                max_count = l1.count(i)
                f_l1.append(i)
        [res.append(j) for j in f_l1 if j not in res]   
        final = final.join(res)
        return(final)

longestCommonPrefix(["dog","racecar","car"])
