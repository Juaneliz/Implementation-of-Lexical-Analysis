"""
Author  : Juan Andrés Elizalde Herrera
Date    : 23-03-2026
Project : DFA Language 50
Purpose : Test cases for the regular expression in regex.py.
          Tests 1-10 must be accepted, tests 11-20 must be rejected.
"""

from dfa_regex import parse, accept

count = 0

# test 1
ans = accept(parse("ab1ba"))
if ans:
    print("passed_1")
    count = count + 1

# test 2
ans = accept(parse("1ba"))
if ans:
    print("passed_2")
    count = count + 1

# test 3
ans = accept(parse("bab1ba"))
if ans:
    print("passed_3")
    count = count + 1

# test 4
ans = accept(parse("1baba"))
if ans:
    print("passed_4")
    count = count + 1

# test 5
ans = accept(parse("aab1ba"))
if ans:
    print("passed_5")
    count = count + 1

# test 6
ans = accept(parse("11ba"))
if ans:
    print("passed_6")
    count = count + 1

# test 7
ans = accept(parse("ab1bba"))
if ans:
    print("passed_7")
    count = count + 1

# test 8
ans = accept(parse("bb1ba"))
if ans:
    print("passed_8")
    count = count + 1

# test 9
ans = accept(parse("1ba1ba"))
if ans:
    print("passed_9")
    count = count + 1

# test 10
ans = accept(parse("abba1ba"))
if ans:
    print("passed_10")
    count = count + 1

# test 11 - must be rejected
ans = accept(parse("ab1"))
if not ans:
    print("passed_11")
    count = count + 1

# test 12 - must be rejected
ans = accept(parse("ba"))
if not ans:
    print("passed_12")
    count = count + 1

# test 13 - must be rejected
ans = accept(parse("1bba"))
if not ans:
    print("passed_13")
    count = count + 1

# test 14 - must be rejected
ans = accept(parse("abba"))
if not ans:
    print("passed_14")
    count = count + 1

# test 15 - must be rejected
ans = accept(parse("ab1b"))
if not ans:
    print("passed_15")
    count = count + 1

# test 16 - must be rejected
ans = accept(parse("1ba1"))
if not ans:
    print("passed_16")
    count = count + 1

# test 17 - must be rejected
ans = accept(parse("bbb"))
if not ans:
    print("passed_17")
    count = count + 1

# test 18 - must be rejected
ans = accept(parse(""))
if not ans:
    print("passed_18")
    count = count + 1

# test 19 - must be rejected
ans = accept(parse("abbb"))
if not ans:
    print("passed_19")
    count = count + 1

# test 20 - must be rejected
ans = accept(parse("1b1bba"))
if not ans:
    print("passed_20")
    count = count + 1

print("passed", count, "of 20")
