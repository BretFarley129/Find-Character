def findChar(arr, char):
    new_list = []
    for i in arr:
        word = i
        if i.find(char) != -1:
            new_list.append(word)
    return new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

print findChar(word_list, char)