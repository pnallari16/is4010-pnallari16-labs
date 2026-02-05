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