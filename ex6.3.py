#ex6.3.py
#word = "banana"
#count = 0
#for letter in word:
    #if letter == "a":
        #count = count + 1
#print(count)

str = input("Enter a word: ")
letter = input("Enter a letter: ")

def count(str, letter):
    count = 0
    for str in str:
        if str == letter:
            count = count + 1
    return count

print(count(str, letter))
