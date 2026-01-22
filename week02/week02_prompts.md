# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> You are a senior Python developer. I have a function that's supposed to sum
> all even numbers in a list, but it's giving wrong results. [```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total]
> Identify the bug and fix the issue
> Provide the corrected code in a Python code block

**AI's Corrected Code:**
[```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        # Change the condition to check if the remainder is 0
        if num % 2 == 0:
            total += num
    return total]

---

## Problem 2: Refactoring

**My Prompt:**
> You are a senior Python developer. I have a function that works correctly, but is written in a confusing, non-Pythonic way [def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results]
> Correct the code so that is written in a Pythonic way. Make sure you refactor it to be more clear, concise, and idiomatic.
>Include list comprehensions, better iteration patterns, or clearer variable names if necessary.
>Provide the corrected code in a Python code block

**AI's Corrected Code:**
[```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users 
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    # Use a list comprehension for a concise, readable, and efficient solution
    return [user['name'] for user in users if user['age'] >= 18]]

---

## Problem 3: Documenting

**My Prompt:**
> You are a senior Python developer. I have a function that works correctly but does not have any documentation.
>The function also raises a ValueError for invalid inputs [def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width]
> Using the code given, write a professional NumPy-style docstring for this function.

**AI's Corrected Code:**
[```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users 
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    # Use a list comprehension for a concise, readable, and efficient solution
    return [user['name'] for user in users if user['age'] >= 18]]

---
