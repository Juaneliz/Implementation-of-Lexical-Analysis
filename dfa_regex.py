"""
Author  : Juan Andrés Elizalde Herrera
Date    : 23-03-2026
Project : DFA Language 50
Purpose : Given a string over the alphabet {a, b, 1}, determine
          if it belongs to the language that contains 'ab1' or '1ba'
          and ends with 'ba'. Returns yes if accepted, no if rejected.
"""

import re

PATTERN = r'^(b|abb|a*(1b)*1bb)*(a+b1(1|a)*((1|a)*b+a)+|a*1+(b1)*ba((1|a)*ba)*)$'

def parse(string):

    return string.strip()

def accept(string):
    return bool(re.match(PATTERN, string))

if __name__ == '__main__':
    inp = str(input())
    res = parse(inp)
    res = accept(res)
    if res:
        print("yes")
    else:
        print("no")
