import sys

def matched(arg:str)->bool:
    """Function to check if every string entry has a matching symbols.
    Params:
    ---------
    arg: <str> input literal/string value.
    
    Returns:
    ---------
    <bool> : True if there is a match; False otherwise."""
    open_braces=0
    close_braces=0
    for i in arg:
        if i == '(':
            open_braces+=1
        elif i == ')':
            close_braces+=1
    if open_braces == close_braces:
        return True
    else:
        return False

if __name__ == "__main__":
    print(matched(sys.argv[1]))
