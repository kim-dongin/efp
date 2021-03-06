# Exercise 2. Counting the Number of Characters
# Output:
#   What is the input string? Homer
#   Homer has 5 characters.
# Constraints:
#   Be sure the output contains the original string.
#   Use a single output statement to construct the output.
#   Use a built-in function of a programming language to determine the length of the string.


#!/usr/bin/env python

import sys

def input_process(in_string):
    return input(in_string) if (3,0) <= sys.version_info else raw_input(in_string)

def main():
    input_string = str(input_process('What is the input string? '))
    counting_string = '%s has %d characters.' % (input_string, len(input_string))
    print(counting_string)

if __name__ == '__main__':
    main()
