s = "()[]{}"

for i in range(len(s)):
    if i == len(s)-1:
        break

    if (s[i] == "(" and s[i+1] != ")") or (s[i] == ")" and s[i-1] != "("):
        print("Nope")
    elif (s[i] == "[" and s[i+1] != "]") or (s[i] == "]" and s[i-1] != "["):
        print("Nope")
    elif (s[i] == "{" and s[i+1] != "}") or (s[i] == "}" and s[i-1] != "{"):
        print("Nope")
    