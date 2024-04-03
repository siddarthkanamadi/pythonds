def reverse_word(word):
    stack=[]
    for character in word:
        stack.append(character)
    reverse_word=""
    while stack:
        reverse_word+=stack.pop()
    return reverse_word
word=input("enter the word:")
print(reverse_word(word))