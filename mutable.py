def change_str(the_string:str, position:int, the_char:str)->str:
    """
    string is immutable. try to find a way to replace a char inside a string to make the string "mutable"
    """
    return the_string[:position] + the_char + the_string[position+1:]

if __name__=="__main__":
    string_from_user=input("Enter string: ")
    position_from_user = int(input("Enter position: "))
    new_char = input("Enter new char: ")
    print(change_str(the_string=string_from_user,
                     position=position_from_user,
                     the_char=new_char))