#Ex6.1
word = input("Enter a word:")
index = -1

negative_len = len(word) * -1

while True:
    if index == negative_len - 1:
        break
    letter = word[index]
    print(letter)
    index = index -1
