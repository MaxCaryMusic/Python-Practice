import os

def print_title(function_name):
    print(f"{function_name} Demo", "*"*20, sep="\n", end="\n"*2)

def pause_terminal():
    input("Press Enter to continue...")
    os.system('clear')

def print_input(*args):
    print("input:", *args)

def print_output(*args):
    print("output:", *args, end="\n"*2)
