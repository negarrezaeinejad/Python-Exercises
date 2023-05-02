# Vehicle Class

This is a simple Python class named Vehicle. The class takes 4 arguments in the constructor and has two methods: brake and drive.

## Class Definition

The class has the following attributes:

- **color**: color of the vehicle
- **doors**: number of doors the vehicle has
- **tires**: number of tires the vehicle has
- **type**: type of the vehicle (e.g., car, truck, motorcycle)

## Methods

### brake()

This method returns the string "{type} braking", where `{type}` is the type of the vehicle.

### drive()

This method returns the string "I am driving a {doors} door {color} {type}", where `{doors}` is the number of doors of the vehicle, `{color}` is the color of the vehicle and `{type}` is the type of the vehicle.

## Example Usage

```python
vehicle = Vehicle('red', 4, 4, 'car')
print(vehicle.brake())
print(vehicle.drive())
```

## Output

```python
car braking
I am driving a 4 door red car.
```