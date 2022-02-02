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
    if step >0:  # step -> positive increment
        if end < start: # additional check to make sure the format is (less,greater,step increment)
            end = end+start
            start = end - start
            end = end - start
            # swapping to make sure we have the proper format
            # Reason for this is that in a function definition, we cannot define non default value after defining default value. 
        while start < end:
            l.append(start)
            start += step
        return l
    else: # step -> negetive increment or decrement value
        if end < start:
            print("Error: First parameter should be greater than the 2nd parameter")
        while end > start:
            l.append(end)
            end = end+step
        return l
    