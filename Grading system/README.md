# Grading System

This Python program takes input from the user for their score and assigns a grade based on the given score. The grading system is based on the range of scores within specific intervals, as defined by the program.

## Example Usage

```python
please enter your score: 24
Your score is not in the correct interval.

please enter your score: 16.852
You got a B
```

## How it works

The program first takes input from the user for their score - represented by the variable `x`. It then uses a series of comparisons to assign a grade to the given score.

The grading system is based on the range of scores within specific intervals, as defined by the program. If the score falls within a certain range, it assigns a corresponding letter grade to the score.

For example, if the score falls between 18 and 20 (inclusive), it assigns an A grade. Similarly, if the score falls between 16 and 18 (exclusive), it assigns a B grade. The program checks each interval in order, and if the score does not fall within any of the specified intervals, it prints a message indicating that the score is not within the correct range.

Overall, this program provides a simple grading system based on a given score and assigns a letter grade accordingly.