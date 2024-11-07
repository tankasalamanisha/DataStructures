from typing import List

def plusOne(digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join([str(i) for i in digits])) + 1)]

if __name__ == "__main__":
    my_list = [1,2,3]

    print(plusOne(my_list))