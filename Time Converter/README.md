# Time Converter

This Python code takes the input of the number of remaining seconds, and converts it into days, hours, minutes, and seconds. The code divides the input seconds by 43200 (number of seconds in a day) to get the number of days, then it takes the modulo of the input seconds with 43200 to get the remaining seconds. It further divides the remaining seconds with 3600 (number of seconds in an hour) to get the number of hours. This process continues to get the number of minutes and seconds.

## Example

```python
Please enter the number of remaining seconds: 354850
8 day(s) 2 hour(s) 34 minute(s) 10 second(s)
```

In this example, the input is 354850 seconds, and the output shows that this is equal to 8 days, 2 hours, 34 minutes, and 10 seconds.