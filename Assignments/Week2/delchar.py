import sys

def delchar(s:str, ch:str)->str:
    """Function to delete given character from the string

    Args:
        s (str): Input string
        ch (str): Input character to be deleted

    Returns:
        str: string with deleted characters.
    """
    return s.replace(ch,'')

if __name__ == "__main__":
    print(delchar(sys.argv[1], sys.argv[2]))