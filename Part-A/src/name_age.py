"""The program is intended to figure out the user's birth year based on their age and the current year.

Input:
    CURRENT_YEAR = date.today().year 
    user_name = input("What is your name?: ")
    user_age = int(input("How old are you?: "))

Process:
    birth_year = (CURRENT_YEAR - user_age)

Output:
    print("Hello", user_name + "!\nYou were born in", birth_year, ".")

Typical usage example:
    What is your name? Crystal 
    How old are you? 25
    Hello Crystal!
    You were born in 2001.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("What is your name?: ")
    user_age = int(input("How old are you?: "))

    # Calculate user's approximate birth year.
    birth_year = (CURRENT_YEAR - user_age)

    # Output personalized message with user's name and birth year.
    print("Hello", user_name + "!\nYou were born in", birth_year, ".")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
