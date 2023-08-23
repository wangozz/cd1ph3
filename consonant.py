def consonant_value(s):
    def char_value(c):
        return ord(c) - ord('a') + 1
    
    max_value = 0
    current_value = 0

    for char in s:
        if char in 'aeiou':
            current_value = 0
        else:
            current_value += char_value(char)
            max_value = max(max_value, current_value)

    return max_value
