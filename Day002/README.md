# Deep Dive Tutorial: Python Data Types

## Introduction

Python is a dynamically typed language, meaning you don't need to declare the type of a variable when you create one. This tutorial will explore the various built-in data types in Python, their characteristics, and how to use them effectively.

## 1. Numeric Types

Python has three main numeric types: `int`, `float`, and `complex`.

### 1.1 Integer (`int`)

- Represents whole numbers, both positive and negative.
- Example:

  ```python
  a = 10
  b = -5
  ```
  ```

### 1.2 Float (`float`)

- Represents real numbers (floating-point numbers) with decimal points.
- Example:
  ```python
  pi = 3.14
  temperature = -10.5
  ```

### 1.3 Complex (`complex`)
- Represents complex numbers, which have a real and an imaginary part.
- Example:
  ```python
  z = 2 + 3j  # 2 is the real part, 3 is the imaginary part
  ```

## 2. Sequence Types
Python has several sequence types, including `list`, `tuple`, and `range`.

### 2.1 List
- A mutable, ordered collection of items.
- Can contain mixed data types.
- Example:
  ```python
  fruits = ['apple', 'banana', 'cherry']
  fruits.append('orange')  # Adding an item
  ```

### 2.2 Tuple
- An immutable, ordered collection of items.
- Can also contain mixed data types.
- Example:
  ```python
  coordinates = (10.0, 20.0)
  ```

### 2.3 Range
- Represents an immutable sequence of numbers, commonly used for looping.
- Example:
  ```python
  for i in range(5):  # Generates numbers from 0 to 4
      print(i)
  ```

## 3. Text Type
### 3.1 String (`str`)
- Represents a sequence of characters.
- Strings are immutable.
- Example:
  ```python
  greeting = "Hello, World!"
  ```

## 4. Mapping Type
### 4.1 Dictionary (`dict`)
- An unordered collection of key-value pairs.
- Keys must be unique and immutable.
- Example:
  ```python
  student = {'name': 'Alice', 'age': 25}
  ```

## 5. Set Types
Python has two types of sets: `set` and `frozenset`.

### 5.1 Set
- An unordered collection of unique items.
- Mutable.
- Example:
  ```python
  unique_numbers = {1, 2, 3, 4, 5}
  ```

### 5.2 Frozenset
- An immutable version of a set.
- Example:
  ```python
  frozen_numbers = frozenset([1, 2, 3, 4, 5])
  ```

## 6. Boolean Type
### 6.1 Boolean (`bool`)
- Represents one of two values: `True` or `False`.
- Example:
  ```python
  is_active = True
  ```

## 7. None Type
### 7.1 None
- Represents the absence of a value or a null value.
- Example:
  ```python
  result = None
  ```

## 8. Type Checking
You can check the type of a variable using the `type()` function.
```python
print(type(a))  # Output: <class 'int'>
print(type(fruits))  # Output: <class 'list'>
```

## 9. Type Conversion
You can convert between different data types using built-in functions:
- `int()`, `float()`, `str()`, etc.
```python
num = 10
num_str = str(num)  # Convert integer to string
```

## Conclusion
Understanding Python's data types is crucial for effective programming. Each type has its own characteristics and use cases, and knowing when to use each can greatly enhance your coding efficiency. Experiment with these data types to become more familiar with their behavior and capabilities.
