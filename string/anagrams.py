from collections import Counter
def is_anagram(s1, s2):
    new_s1 = "".join(s1.lower().split())
    new_s2 = "".join(s2.lower().split())

    char_counts_s1 = Counter(new_s1)
    char_counts_s2 = Counter(new_s2)

    if char_counts_s1 == char_counts_s2:
        return True 
    else:
        return False
    
if __name__ == "__main__":
    s1 = input('Please enter the first string: ')
    s2 = input('Please enter the second string: ')

    if is_anagram(s1, s2): 
        print('Anagrams')
    else:
        print('Not anagrams')
