def encode_caesar_string(s, n): 
    if not n.isdigit(): 
        print("This is not a valid shift")
        return None
    n = int(n)
    if n not in range(1,26): 
        print("This is not a valid shift")
        return None 
    else: 
        new_s = ''
        for char in s: 
            if not char.isalpha():
                new_s += char
                continue
            code = ord(char) + n
            if char.isupper() and code > ord('Z'):
                code = ord('A') + abs(ord('Z')-code) - 1
            if char.islower() and code > ord('z'):
                code = ord('a') + abs(ord('z')-code) - 1
            new_s += chr(code)
    return new_s

if __name__ == "__main__":
    s = input('Please enter string: ')
    n = input('Please enter the shift: ')

    print(encode_caesar_string(s, n))



