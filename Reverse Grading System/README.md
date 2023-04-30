# Reverse Grading System

This Python code prompts the user to enter a letter grade (A, B, C, D, E, or F) and then prints the corresponding range of scores. The score ranges are as follows:

- A: 18 <= score <= 20
- B: 16 <= score < 18
- C: 14 <= score < 16
- D: 12 <= score < 14
- E: 10 <= score < 12
- F: 0 <= score < 10 (failed)

If the user enters an invalid letter grade, the program will print a message stating that the score is not correctly entered.

Example:

```python
please enter your score: e
You got a score between 10 and 11.9999...

please enter your score: L
Your score is not correctly entered.
```