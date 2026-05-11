def is_palindrome(s):
    if s == "":
        return False
    new_s = "".join(s.lower().split())
    half = len(s)//2
    for index, char in enumerate(new_s[:half]):
        if char != new_s[-(index+1)]:
            return False
    return True

if __name__ == "__main__":
    s = input('Please enter a string: ')
    if is_palindrome(s) == True: 
        print('It\'s a palindrome')
    else:
        print('It\'s not a palindrome')