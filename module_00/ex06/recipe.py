import sys

cookbook = {
    "Sandwich": {"ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
                 "meal": "lunch",
                 "prep_time": 10},
    "Cake":     {"ingredients": ['flour', 'sugar', 'eggs'],
                 "meal": "dessert",
                 "prep_time": 60},
    "Salad":     {"ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
                  "meal": "lunch",
                  "prep_time": 15}
}

options = {
    "1": "add a recipe",
    "2": "delete a recipe",
    "3": "print a recipe",
    "4": "print the cookbook",
    "5": "quit",
}


def print_a_recipe():
    """
    Print the recipe received as a parameter.
    """
    recipe = input("\nWhich recipe do you want to print ?\n")
    if recipe.title() in cookbook.keys():
        print(f"\nThe recipe for a {recipe.title()} is:")
        for step in cookbook[recipe.title()]:
            print(f"- {step}: {cookbook[recipe.title()][step]}")
    else:
        print(f"Sorry, '{recipe}' does not exist in the cookbook.")


def print_the_cookbook():
    """
    Print all the recipe's names in the cookbook.
    """
    print("\nHere are all the recipes in the Cookbook !")
    for recipe in cookbook.items():
        print(f"\t- {recipe[0]}.")


def delete_a_recipe():
    """
    Delete the recipe received as a parameter in the cookbook.
    """
    recipe = input("\nWhich recipe do you want to delete \
from the Cookbook ?\n")
    if recipe.title() in cookbook.keys():
        cookbook.pop(recipe.title())
        print(f"{recipe.title()} has been deleted.")
    else:
        print(f"Sorry, '{recipe}' does not exist in the cookbook.")


def add_a_recipe():
    """
    Add the recipe added by the user in the cookbook.
    """
    new_recipe = input("\nWhat's the name of the new recipe ?\n")
    if new_recipe.title() in cookbook.keys():
        return (print("Recipe already in the cookbook."))

    ingredients = []
    print("\nWhat's the list of ingredients ? \
Ctrl + d or newline when you've done.\n")
    while True:
        try:
            ingredient = input(">> ")
            if ingredient == "":
                if ingredient == "" and len(ingredients) != 0:
                    break
                else:
                    print("Please, select at least 1 ingredient.")
            else:
                ingredients.insert(len(ingredients), ingredient)
        except EOFError:
            if len(ingredients) != 0:
                break
            print("Please, select at least 1 ingredient.")

    meal = input("\nWhat's the meal type ?\n")
    while meal.isalpha() is False:
        meal = input("Only alphabetic input please. What's the meal:\n")

    prep = input("\nWhat's preparation time ?\n")
    while prep.isdecimal() is False:
        prep = input("Only interger please. Write the preparation time:\n")

    cookbook[new_recipe.title()] = {"ingredients": ingredients,
                                    "meal": meal,
                                    "prep_time": prep}
    print("\nThe recipe is now added to the cookbook !")


def print_message_and_list(string):
    """
    Print the message you wanted to write, then the option's list
    """
    print(f"{string}\nChoose an option from the list:")
    for key, value in options.items():
        print(f"\t{key}: {value}")


def receive_input():
    """
    Check if the input is OK, then return the Key of the Cookbook.
    """
    recv = input("\nPlease select an option: ")
    if recv in options.keys():
        if recv == "5":
            print("\nCookbook closed. Goodbye !")
            sys.exit(0)
        return (options[recv].replace(" ", "_"))
    else:
        print_message_and_list("\nSorry, this option does not exist.")
        return False


if __name__ == "__main__":
    print_message_and_list("Welcome to the Python Cookbook !")
    while (True):
        try:
            value = receive_input()
            if value:
                func = locals()[value]
                func()
        except (AttributeError, KeyboardInterrupt, EOFError):
            print("\nCookbook closed. Goodbye !")
            sys.exit(0)
        except Exception as err:
            print(f"Error: {err}")
            sys.exit(0)
