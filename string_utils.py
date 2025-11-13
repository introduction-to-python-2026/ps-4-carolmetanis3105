def split_before_each_uppercases(formula):
    parts = []
    current = ""
    
    for char in formula:
        if char.isupper():
            if current:
                parts.append(current)
            current = char
        else:
            current += char
    if current:
        parts.append(current)
    
    return parts

def split_at_first_digit(formula):
    prefix = ""
    number_part = ""
    
    for char in formula:
        if char.isdigit():
            number_part += char
        elif number_part == "":
            prefix += char
        else:
            number_part += char
    
    if number_part:
        digits = ""
        for c in number_part:
            if c.isdigit():
                digits += c
            else:
                break
        return (prefix, int(digits))
    
    return (formula, 1)
