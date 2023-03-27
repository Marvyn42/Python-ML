from sys import exit as sys_exit
from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if (type(name) != str or len(name) == 0):
            sys_exit("Value Error: book's name should be a non-zero string.")
        self.NAME = name
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.CREATION_DATE = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.recipes_list = {"starter": [],
                             "lunch": [],
                             "dessert": []}

    def __str__(self):
        """Return the string to print with the book info"""
        recipe_list = []
        for recipe_type in ["starter", "lunch", "dessert"]:
            for elem in self.recipes_list[recipe_type]:
                recipe_list.append(elem.name)
        if (len(recipe_list) == 0):
            recipe_string = ""
        else:
            recipe_string = "It contains:\n\t" + ",\n\t".join(recipe_list)
        return (f"\n\tRecipe book: {self.NAME}\n"
                + f"\nCreated: {self.CREATION_DATE}"
                + f"\nUpdated: {self.CREATION_DATE}\n"
                + recipe_string)

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        if (type(name) != str or name == ""):
            print("ValueError: name must be a non-zero string.")
            return
        for _, recipe_list in self.recipes_list.items():
            for recipe in recipe_list:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("NotFound: the recipe you'r searching fort doesn't exist.")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("ValueError: recipe type must be starter, lunch or dessert.")
            return
        liste = [elem.name for elem in self.recipes_list[recipe_type]]
        return (liste)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if (type(recipe) != Recipe):
            print("ValueError: The book receive recipes only.")
            return
        for elem in self.recipes_list[recipe.recipe_type]:
            if elem.name == recipe.name:
                print(f"{recipe.name}: already exist in the book, "
                      + "cannot add it again")
                return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
