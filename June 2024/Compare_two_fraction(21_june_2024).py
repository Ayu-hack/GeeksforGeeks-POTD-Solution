def compare_fractions(s):
    f1,f2= s.split(', ') # split the input in two separate variables using ", " delimeter
    #evaluating the values of each and store them in another variables
    val1 = eval(f1)
    val2 = eval(f2)
    #checking which is bigger
    if val1 > val2:
        return str(f1)
    elif val1 < val2:
        return str(f2)
    else:
        return "equal"
print(compare_fractions(input()))
