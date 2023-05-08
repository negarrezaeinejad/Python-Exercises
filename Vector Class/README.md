# Vector Class

This is a Python class that represents a mathematical vector in a two-dimensional plane. It includes various methods for performing mathematical operations with vectors, such as addition, multiplication, and subtraction, as well as methods for computing the absolute value and negation of a vector.

## Usage

To create a new vector, simply call the `Vector` class with the x and y coordinates as arguments:

```python
v = Vector(3, 4)
```

You can then access the x and y coordinates using the `x` and `y` properties:

```python
print(v.x) # 3
print(v.y) # 4
```

You can also print the vector using the `print` function or the `__str__` method:

```python
print(v)  # (3, 4)
```

Various mathematical operations are defined for vectors, including addition, multiplication, and subtraction:

```python
u = Vector(-5, 4)
z = Vector(3, 4)

print(u + v)   # (-2, 8)
print(u * v)   # -8
print(u - v)   # (-8, 0)
print(u < v)   # True
print(u <= v)  # True
print(z == v)  # True
print(z == u)  # False
```

You can also compute the absolute value of a vector or its negation:

```python
print(abs(v))  # 5.0
print(-v)      # (-3, -4)
```

## Example

```python
if __name__ == "__main__":
    v = Vector(3.0, 4)
    u = Vector(-5, 4)
    z = Vector(3, 4)
    print(f"v={v}")
    print(f"u={u}")
    print(f"-v={-v}")
    print(f"~v={~v}")
    print(f"abs(v)={abs(v)}")
    print(f"u+v = {u+v}")
    print(f"u*v = {u*v}")
    print(f"u-v = {u-v}")
    print(f"u<v = {u<v}")
    print(f"u<=v = {u<=v}")
    print(f"z==v = {z==v}")
    print(f"z==u = {z==u}")
```

### Output

```python
scssCopy code
v=(3,4)
u=(-5,4)
-v=(-3,-4)
~v=(4,3)
abs(v)=5.0
u+v = (-2,8)
u*v = -8
u-v = (-8,0)
u<v = True
u<=v = True
z==v = True
z==u = False
```