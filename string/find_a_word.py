def find_a_word(s, S): 
    list_word = list(s)
    index = 0
    count = 1
    for char in list_word:
        idx = S.lower().find(char, index)
        if idx == -1:
            count = 0
            return 'No'
        else:
            index = max(idx, index)
    if count == 1: 
        return 'Yes'

if __name__ == "__main__":
    s = input('Please enter the first string: ')
    S = input('Please enter the second string: ')

    print(find_a_word(s, S))
