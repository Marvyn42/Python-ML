from sys import exit as sys_exit


class Recipe:
    """Class that's allow you to store a recipe"""

    def __init__(self, name, c_lvl, c_time, ingredients, description, type):
        self.check_args(name, c_lvl, c_time, ingredients, description, type)
        self.name = name
        self.cooking_lvl = c_lvl
        self.cooking_time = c_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = type

    def __str__(self):
        """Return the string to print with the recipe info"""
        ingredients = ", \n\t- ".join(self.ingredients)
        return (f"\n\tRecipe: {self.name}\n\n"
                + f"Difficulty: {self.cooking_lvl}/5,\n"
                + f"It takes {self.cooking_time} minute(s) to prepare,\n"
                + f"The recipe is for {self.recipe_type},\n"
                + f"ingredients:\n\t- {ingredients}\n"
                + f"description: {self.description}"
                )

    @staticmethod
    def check_args(name, c_lvl, c_time, ingredients, description, r_type):
        dic_test = {str: {"name": name, "description": description,
                          "recipe type": r_type},
                    int: {"cooking level": c_lvl, "cooking time": c_time},
                    list: {"ingredients": ingredients}}

        for _type, _dict in dic_test.items():
            for arg_name, arg in _dict.items():
                if isinstance(arg, _type) is False:
                    sys_exit(f"{arg_name} is not {_type}")

        for elem in ingredients:
            if (type(elem) is not str):
                sys_exit("ValueError: Ingredients must contains string only.")
            if (len(elem) == 0):
                sys_exit(
                    "ValueError: An ingredient cannot be an empty string.")
        if (c_lvl not in range(1, 5)):
            sys_exit("ValueError: cooking level should be between 1 and 5.")
        if (c_time < 0):
            sys_exit("ValueError: cooking time couldn't be negative.")
        if (name == ""):
            sys_exit("ValueError: name couldn't be empty.")
        if (r_type not in ["lunch", "starter", "dessert"]):
            sys_exit(
                "ValueError: recipe type must be for starter/lunch/dessert.")
