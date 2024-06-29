def is_palindrome(word):
    for i in range(len(word)):
        word_len = len(word) - i - 1
        if word[i] != word[word_len]:
            return False
    return True


print(is_palindrome("x"))

s = "babad"
l1 = []
for count, value in enumerate(s):
    for i in range