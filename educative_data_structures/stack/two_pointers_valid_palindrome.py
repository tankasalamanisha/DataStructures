import sys
def is_palindrome(value:str)->bool:
    """
    Function to check if the given string is a valid palindrome or not
    Args:
    ----------------------
    value(str) : Input string.

    Return:
    -----------------------
    bool : Truth value to check whether or not the given string is a palindrome.

    Space Complexity:

    After executing this function, I understood that the space complexity of this implimentation is O(1) as it needs a constant space. The other parameters like
    start, end are used only for keeping track of the pointers/ placeholders and are calculated on the fly. The functions like zip and range also are in-built and 
    do not require additional space. 

    Time Complexity:
    The time complexity required for this is O(n) for a single iteration, where n-> size of the string. As two-pointers makes sure its traversal is tracked on
    both sides using a single iteration through zip function, the iteration length accounts for the time complexity.
    Edit : added another condition: if start < end, so the time complexity now is o(n/2) as the for loop traverses only half way.
    """
    for start, end in zip(range(0,len(value)), range(len(value)-1,-1,-1)):
        if (value[start] != value[end]) & (start < end):
            return False
    return True


if __name__ == "__main__":
    input_string = sys.argv[1]
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome!")
    else:
        print(f"{input_string} is not a palindrome!")