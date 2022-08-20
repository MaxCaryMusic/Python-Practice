from helpers import print_input

def function_one(first_var):
    print_input(first_var)
    return first_var

def function_two(first_var, second_var):
    print_input(first_var, second_var)
    return first_var, second_var

def function_three(*first_var):
    print_input(*first_var)
    return *first_var, first_var

def function_four(first_var, second_var, third_var=None, fourth_var="test"):
    print_input(first_var, second_var, third_var, fourth_var)
    return {"first_var": first_var, "second_var": second_var, "third_var": third_var, "fourth_var": fourth_var}

def function_five(first_var="test", second_var=None):
    print_input(first_var, second_var)
    return first_var, second_var

def function_six(*first_var, **second_var):
    print_input(*first_var, second_var)
    return *first_var, second_var
