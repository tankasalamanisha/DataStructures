from utils import Stack

def is_paranthesis_balanced(paranthesis_string):
    s = Stack()
    is_balanced = True
    i=0

    while i < len(paranthesis_string) and is_balanced:
        string_considered=paranthesis_string[i]

        if string_considered in "({[":
            s.push(string_considered)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top,string_considered):
                    is_balanced = False
                    break
        i += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def is_match(paranthesis1, paranthesis2):
    if paranthesis1 == "(" and paranthesis2 == ")":
        return True
    elif paranthesis1 == "[" and paranthesis2 =="]":
        return True
    elif paranthesis1 == "{" and paranthesis2 == "}":
        return True
    else:
        return False

if __name__ == "__main__":

    print("String : (((({})))) Balanced or not?")
    print(is_paranthesis_balanced("(((({}))))"))

    print("String : [][]]] Balanced or not?")
    print(is_paranthesis_balanced("[][]]]"))

    print("String : [][] Balanced or not?")
    print(is_paranthesis_balanced("[][]"))