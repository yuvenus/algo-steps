# Author: Venus Yu
import math

# 1. Read input.
n = int(raw_input())

# 2. Do your algorithm.

def minSteps(n):
    steps = 0
    remain = n
    currStep = 1
    
    while True:
        if remain == 1:
            steps = 1
            return 1
    
        remain -= 2 * currStep
        steps += 2
        currStep += 1
        if (remain/2 < currStep):
            break

    if remain > currStep:
        steps += 2
    elif remain != 0:
        steps += 1
    return steps


# 3. Write output.
print minSteps(n)
