# ********
# This file is individualized for NetID huxing.
# ********

import traceback
import sys

def format(value):
    if type(value) == str: return "'%s'" % value
    if type(value) == type(format): return value.__name__
    return str(value)

def run_test(function, arguments, target):
    print("Testing %s(%s):" % (function.__name__, ", ".join(map(format, arguments))))
    try:
        output = function(*arguments)
        if function(*arguments) == target:
            print("    PASSED: Score = 2 of 2")
            return 2
        else:
            print("    FAILED: Score = 1 of 2")
            print("    Target output: " + format(target))
            print("    Actual output: " + format(output))
            return 1
    except Exception as error:
        print("    CRASHED: Score = 0 of 2")
        traceback.print_tb(error.__traceback__)
        print("    %s: %s" % (type(error).__name__, error))
        return 0

def run_tests(test_data):
    total_score = 0
    for args in test_data:
        total_score += run_test(*args)
    return total_score

if __name__ == "__main__":
    
    from helpers import *

    def grub_test_ai(day, rent_payment, balance, chickens, eggs, grubs):
        return min(chickens * 9, max_grubs(balance))

    def dozen_test_ai(day, rent_payment, balance, chickens, eggs, grubs):
        return max_dozens(eggs, day)
    
    test_data = [

        (next_day, ("Monday",), "Tuesday"),
        (next_day, ("Tuesday",), "Wednesday"),
        (next_day, ("Sunday",), "Monday"),
        
        (max_grubs, (1.0,), 20),
        (max_grubs, (123456.7,), 900),

        (max_dozens, (10, "Monday"), 0),
        (max_dozens, (200, "Friday"), 3),
        (max_dozens, (200, "Thursday"), 2),
        (max_dozens, (20, "Monday"), 1),

        (measure_feed, (38, 3), 27),
        (measure_feed, (21, 3), 18),

        (slaughter_chickens, (38, 3), 0),
        (slaughter_chickens, (21, 3), 1),

        (lay_eggs, (0,), 0),
        (lay_eggs, (1,), 11),
        (lay_eggs, (2,), 11),
        (lay_eggs, (3,), 13),
        (lay_eggs, (4,), 16),

        (hatch, (100,), 20),
        (hatch, (12,), 2),
        (hatch, (1,), 0),
        
    ]
    total_score = run_tests(test_data)
    print("")

    print("Total score: %d out of %d" % (total_score, len(test_data)*2))

