def process_input_string(input_str:str)->str:
    """
        Compresses a string by counting consecutive characters.
        For example, "aaabb" becomes "a3b2".
    """

    if not input_str:
        return ""

    result=[]
    prev_char=input_str[0]
    counter = 0
    for char in input_str:
        if char == prev_char:
            counter+=1
        else:
            result.append(f"{prev_char}{counter}")
            counter = 1
        prev_char = char

    result.append(f"{prev_char}{counter}")
    return ''.join(result)

if __name__ == "__main__":
    print(process_input_string("aaaaeebbbrccyyyyyyyttpvzxzzzzzzzzzza"))


