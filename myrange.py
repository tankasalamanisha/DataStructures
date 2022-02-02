def my_range(end , start =0, step=1):
    """"
    Custom range() function.
    Parameters:
    ------------
    end: range upto which numbers need to be generated.
    start: starting point of the numbers; default = 0.
    step: incrementing value for generating the list of numbers.
    
    Note: if step is a negetive number, then make sure to enter end greater than start.

    Return:
    ------------
    l: list of sequenced numbers based on the step."""
    l=[]
    if step >0:
        if end < start:
            end = end+start
            start = end - start
            end = end - start
        while start < end:
            l.append(start)
            start += step
        return l
    else:
        if end < start:
            print("Error: First parameter should be greater than the 2nd parameter")
        while end > start:
            l.append(end)
            end = end+step
        return l
    