# Clock Simulator Class

This Python code defines a class called `Clock` that simulates a clock. The `Clock` class has the following properties and methods:

## Properties

- `hour`: an integer between 0 and 23, representing the hour of the clock.
- `minute`: an integer between 0 and 59, representing the minute of the clock.
- `second`: an integer between 0 and 59, representing the second of the clock.

## Methods

- `__init__`: initializes the `Clock` object with a given `hour`, `minute`, and `second` values or with the current system time.
- `__str__`: returns a string representation of the `Clock` object in the format "hh:mm:ss".
- `__repr__`: returns a string representation of the `Clock` object, with an "AM" or "PM" suffix depending on the hour value.
- `tik`: advances the clock by one second.
- `__next__`: advances the clock by one second and rings if the time is midnight. Returns the `Clock` object.
- `isMidnight`: returns a Boolean value indicating whether the clock is at midnight.
- `ring`: produces a ringing sound if the clock is at midnight.
- `run`: prints the time of the `Clock` object every second and advances the clock by one second.

The `Clock` class is initialized with default values of 10:10:23, or it can be initialized with a specific time using the `hour`, `minute`, and `second` arguments. The `op` argument specifies whether to use the given time or the current system time.

An example usage of the `Clock` class is also provided. It initializes a `Clock` object with the time 23:59:00 and advances the clock by one second 60 times, printing the current time each time. The output of the example is saved in the file `output.txt`.

## Example Output

```python
23:59:01
23:59:02
23:59:03
23:59:04
23:59:05
23:59:06
23:59:07
23:59:08
23:59:09
23:59:10
23:59:11
23:59:12
23:59:13
23:59:14
23:59:15
23:59:16
23:59:17
23:59:18
23:59:19
23:59:20
23:59:21
23:59:22
23:59:23
23:59:24
23:59:25
23:59:26
23:59:27
23:59:28
23:59:29
23:59:30
23:59:31
23:59:32
23:59:33
23:59:34
23:59:35
23:59:36
23:59:37
23:59:38
23:59:39
23:59:40
23:59:41
23:59:42
23:59:43
23:59:44
23:59:45
23:59:46
23:59:47
23:59:48
23:59:49
23:59:50
23:59:51
23:59:52
23:59:53
23:59:54
23:59:55
23:59:56
23:59:57
23:59:58
23:59:59
00
```