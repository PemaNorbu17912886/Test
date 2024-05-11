def find_first_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char, id(char)
        else:
            char_count[char] = 1
    
    
    return None

result = find_first_repeating_character("programming")
if result is None:
    print("No repeating character found.")
