
digit_to_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def pairs(set1, set2):
    result = []
    for letters_1 in set1:
        for letters_2 in set2:
            result.append(letters_1 + letters_2)
    return result

if len(digits) == 0:
    return ""

if len(digits) == 1:
    return digit_to_letters[digits[0]]

if len(digits) == 2:
    return pairs(digit_to_letters[digits[0]], digit_to_letters[digits[1]])

elif len(digits) == 3:
    res = pairs(digit_to_letters[digits[0]], digit_to_letters[digits[1]])
    return pairs(res, digit_to_letters[digits[2]])

else:
    res1 = pairs(digit_to_letters[digits[0]], digit_to_letters[digits[1]])
    res2 = pairs(digit_to_letters[digits[2]], digit_to_letters[digits[3]])
    
    return pairs(res1, res2)