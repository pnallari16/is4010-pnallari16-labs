## Problem 1 Prompt: 
I have a problem and would like you to solve it. Create a python function that finds the common elements between 2 lists. Scenario: You have two very large lists of product IDs from two different suppliers. You need to find out which product IDs are present in both lists so you know which products you can source from either supplier. The order of the final list does not matter. 

### Code

```python
def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    This function should take two lists and return a new list containing
    only the elements that are present in both input lists. The final
    list can be in any order.

    Parameters
    ----------
    list1 : list
        The first list of elements.
    list2 : list
        The second list of elements.

    Returns
    -------
    list
        A list of elements common to both list1 and list2.
    """
    pass
```

## AI Response

When you're dealing with "very large lists," efficiency is the name of the game.If you were to compare every item in the first list to every item in the second list using a loop, your computer would be doing a massive amount of work ($O(n \times m)$ complexity). Instead, we use a Set. In Python, looking up an item in a set happens almost instantly, regardless of how large the set is.The Python CodePythondef find_common_elements(list1, list2):
    """Find the common elements between two lists."""
    
    # Converting the lists to sets allows for high-speed comparisons.
    # This is much faster for large datasets than nested loops.
    set1 = set(list1)
    set2 = set(list2)
    
    # The '&' operator finds the 'intersection' (elements in both).
    common_elements = set1 & set2
    
    # Return the result as a list as requested.
    return list(common_elements)

# --- Testing the function ---
if __name__ == "__main__":
    supplier_a = ["PROD-101", "PROD-202", "PROD-505", "PROD-999"]
    supplier_b = ["PROD-505", "PROD-101", "PROD-707", "PROD-808"]
    
    matches = find_common_elements(supplier_a, supplier_b)
    
    print(f"Common Product IDs: {matches}")
Why this is the best approach:Performance: For a list with 100,000 items, a standard loop could take several seconds (or even minutes) to finish. Using set intersection usually takes just a few milliseconds.Readability: Using the & operator is the "Pythonic" way to handle intersections. It clearly shows you are looking for where the two groups overlap.Uniqueness: Sets automatically remove duplicates. If Supplier A accidentally listed "PROD-101" twice, this function will still correctly return it just once in your common list.

---

## Problem 2 Prompt: 
 
I have a problem and would like you to solve it. Create a python function for the following scenario: Your application loads a list of user profiles from a database. Each user has a unique username, an age, and an email address. You frequently need to look up a user's complete profile by their username. Performance is critical. Here is the given code:
### Code

```python
 def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    ----------
    users : list of dict
        A list of dictionaries, where each dictionary represents a user
        and has 'name', 'age', and 'email' keys. It is recommended to
        convert this list into a more efficient data structure for lookups.
    name : str
        The name of the user to find.

    Returns
    -------
    dict or None
        The dictionary of the found user, or None if no user is found.
    """
    pass

```

## AI Response

Since performance is critical for frequent lookups, a dictionary is the best data structure to use.In your current setup, searching through a list requires checking every single item until you find a match ($O(n)$ time complexity). By converting that list into a dictionary (hash map) where the username is the key, the lookup time becomes nearly instantaneous ($O(1)$ time complexity), regardless of how many millions of users you have.The Python CodeI have provided the function logic and a "preprocessing" step, which is standard practice when you need to perform multiple high-performance lookups.Pythondef find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data."""
    
    # STEP 1: Optimization
    # Convert the list of dicts into a single dictionary for O(1) lookup.
    # We use a dictionary comprehension: {key: value}
    user_lookup_map = {user['name']: user for user in users}
    
    # STEP 2: Lookup
    # We use .get() so that if the name doesn't exist, it returns None
    # instead of crashing the program.
    return user_lookup_map.get(name)

# --- Example Usage & Testing ---
if __name__ == "__main__":
    # Simulated database load
    user_list = [
        {'name': 'alice_92', 'age': 31, 'email': 'alice@example.com'},
        {'name': 'bob_builder', 'age': 45, 'email': 'bob@construction.com'},
        {'name': 'charlie_brown', 'age': 10, 'email': 'charlie@peanuts.com'}
    ]
    
    # Finding a user
    target = "bob_builder"
    profile = find_user_by_name(user_list, target)
    
    if profile:
        print(f"Profile found for {target}: {profile}")
    else:
        print("User not found.")
Why this approach wins on performance:
Hash Map Advantage: Python dictionaries use hash tables. Instead of "scanning" the list like a human reading a book, Python calculates a "hash" for the name and jumps directly to that spot in memory.
Scalability: If your user list grows from 100 to 1,000,000, a list search gets 10,000 times slower. A dictionary lookup stays exactly the same speed.
Safety: Using .get(name) is a "defensive" coding practice. It prevents KeyError exceptions if you try to look up a username that doesn't exist in your database.
Important Implementation Note:If you are calling this function thousands of times, you shouldn't convert the list to a dictionary inside the function (because the conversion itself takes time). Instead, you should convert the list once at the start of your program and just use the resulting dictionary for all your lookups.
---

## Problem 3 Prompt: 
I have a problem and would like you to solve it. Create a python function for the following scenario: You are given a list of integers representing sensor readings. You need to produce a report that contains only the even-numbered readings, and they must be presented in the exact same order they were received. Here is the given code: 

### Code

```python
def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    list of int
        A new list containing only the even integers from the input list.
    """
    pass
```

## AI Response

To filter these sensor readings while maintaining their original order, the most efficient and "Pythonic" way is to use a List Comprehension.

In Python, we check if a number is even by using the modulo operator %. If number % 2 equals 0, it means there is no remainder when divided by 2, identifying it as an even number.

The Python Code
Python
def get_list_of_even_numbers(numbers):
    """
    Return a new list containing only the even numbers from the input list.
    """
    
    # Using a list comprehension to filter the list.
    # This reads like a sentence: "Give me 'n' for every 'n' in 'numbers' IF 'n' is even."
    even_readings = [n for n in numbers if n % 2 == 0]
    
    return even_readings

# --- Testing the function ---
if __name__ == "__main__":
    # Example sensor data
    sensor_data = [15, 22, 34, 41, 56, 78, 93, 100]
    
    report = get_list_of_even_numbers(sensor_data)
    
    print(f"Original Readings: {sensor_data}")
    print(f"Even-Numbered Report: {report}")
Why this approach is effective:
Preserves Order: List comprehensions iterate through the input list from index 0 to the end, ensuring your report follows the exact timeline of the sensor readings.

Memory Efficient: It creates a new list without modifying the original data, which is important if you need the raw sensor_data for other reports later.

The Modulo Operator: * 10 % 2 == 0 (True, even)

11 % 2 == 1 (False, odd)

---