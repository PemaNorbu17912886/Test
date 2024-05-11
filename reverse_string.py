def reverse_string(s):
    
    if len(s) <= 1:
        return s
    else:
        
        first_char = s[0]
        remaining_chars = s[1:]
        
        reversed_remaining = reverse_string(remaining_chars)
        
        return reversed_remaining + first_char


print(reverse_string("hello"))   
print(reverse_string("python"))  
print(reverse_string(""))        
