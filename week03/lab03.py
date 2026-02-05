def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.

    Examples
    --------
    >>> generate_mad_lib("silly", "cat", "jumped")
    "The silly cat jumped over the lazy dog and laughed."
    
    >>> generate_mad_lib("brave", "knight", "battled") 
    "Once upon a time, a brave knight battled dragons and saved the kingdom."
    """
    # TODO: Replace this with your creative story implementation
    # Must use f-string formatting and include all three parameters
    # Using an f-string to insert the variables into the template
    story = f"Yesterday, the {adjective} {noun} {verb} through the busy city streets, causing all the pedestrians to drop their ice cream cones in shock."
    
    return story

# --- Testing the function ---
if __name__ == "__main__":
    # Test Case 1 (The example provided)
    print("Test 1:")
    print(generate_mad_lib("silly", "cat", "jumped"))
    
    print("-" * 20)
    
    # Test Case 2 (A new combination)
    print("Test 2:")
    print(generate_mad_lib("shiny", "robot", "danced"))
    
    print("-" * 20)
    
    # Test Case 3 (Another combination)
    print("Test 3:")
    print(generate_mad_lib("angry", "toaster", "exploded"))



import random

def guessing_game():
    """
    Plays a number guessing game with the user.
    
    This interactive game demonstrates while loops, conditionals, and user input
    handling. The user attempts to guess a randomly generated number between
    1 and 100, receiving feedback after each guess.

    Game Flow:
    1. Generate a random secret number between 1 and 100 (inclusive)
    2. Prompt the user with clear instructions
    3. Use a while loop to continue until the user guesses correctly
    4. For each guess:
       - Convert user input to integer
       - Compare guess to secret number
       - Provide feedback: "Too high!", "Too low!", or success
       - Count attempts
    5. When correct, congratulate user and show number of attempts
    6. Exit the game

    Input Validation:
    - Assume user will enter valid integers (error handling not required)
    
    Example Game Session:
    --------
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Enter your guess: 50
    Too high! Try again.
    Enter your guess: 25
    Too low! Try again.
    Enter your guess: 37
    Congratulations! You guessed it in 3 attempts!
    """
    # 1. Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    # 2. Clear welcome message
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you figure out what it is?")
    print("-" * 30)

    # 3. Use a while loop to continue until the user guesses correctly
    while not guessed_correctly:
        # 4. Prompt for input and convert to integer
        user_input = input("Enter your guess: ")
        current_guess = int(user_input)
        attempts += 1

        # Compare guess to secret number
        if current_guess > secret_number:
            print("Too high! Try again.")
        elif current_guess < secret_number:
            print("Too low! Try again.")
        else:
            # 5. Success!
            guessed_correctly = True
            print(f"Congratulations! You guessed it in {attempts} attempts!")

# To run the game:
if __name__ == "__main__":
    guessing_game()   