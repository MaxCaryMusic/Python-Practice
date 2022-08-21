from helpers import print_output, print_title, pause_terminal
from demo_funcs import function_one, function_two, function_three, function_four, function_five, function_six


print_title("Function One")

test_var = function_one("test1")
print("output:", test_var, end="\n"*2)

try:
    test_var = function_one("test1")
except Exception as err:
    print_output(err)

pause_terminal()


print_title("Function Two")

test_var = function_two("test1", "test2")
print_output(test_var)

test_var_1, test_var_2 = function_two("test1", "test2")
print_output(test_var_1, test_var_2)

try:
    test_var_1, test_var_2 = function_two("test1", "test2")
except Exception as err:
    print_output(err)

try:
    test_var_1, test_var_2 = function_two("test1", "test2")
except Exception as err:
    print_output(err)

pause_terminal()

print_title("Function Three")

test_var = function_three("test1", "test2")
print_output(test_var)

try:
    test_var_1, test_var_2, test_var_3 = function_three("test1", "test2")
except Exception as err:
    print_output(err)


test_var_1, test_var_2, test_var_3 = function_three("test1", "test2")
print_output(test_var_1, test_var_2, test_var_3)


