# Week 3 Assignment: Grade Reporter & Bug Hunt

This repository contains Python programs demonstrating the use of loops, conditional statements, and debugging techniques.

## Files
- `grade_reporter.py`: Calculates grades for a list of scores, counts passes/fails, and computes the average score.
- `bug_hunt.py`: A debugged program that correctly calculates and displays the sum of numbers from 1 to 5.

## Bug Hunt Reflection
The hardest bug to find in Part B was the logic bug where the loop condition was set to `count < 5` instead of `count <= 5`. Since Python executed the code without raising any syntax or runtime errors, the program appeared to work fine on the surface. However, I knew something was wrong because the final printed sum was 10 instead of the expected correct sum of 15.
