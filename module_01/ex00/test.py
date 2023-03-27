from sys import exit as sys_exit
from recipe import Recipe
from book import Book

if __name__ == "__main__":
    pizza = Recipe("pizza", 3, 15, ["pasta", "tomatoes", "cheese", "Olive"],
                   "", "lunch")
    cookies = Recipe("cookies", 2, 20, ["flour", "chocolate", "butter"],
                     "masterclass", "dessert")
    shaker = Recipe("shaker", 1, 5, ["milk", "protein pouder"],
                    "", "dessert")
    salad = Recipe("salad", 2, 20, ["salad", "cheese", "tomatoes", "vinegar"],
                   "", "starter")

    myBook = Book("myBook")
    print(myBook)
    print("--------------------------------------")
    myBook.add_recipe(pizza)
    print(myBook)
    print("--------------------------------------")

    myBook.add_recipe(cookies)
    myBook.add_recipe(shaker)
    myBook.add_recipe(salad)
    print(myBook)
    print("--------------------------------------")
    myBook.add_recipe(salad)
    print("--------------------------------------")
    myBook.add_recipe(798)
    myBook.add_recipe("798")
    print("--------------------------------------")

    liste = myBook.get_recipes_by_types("dessert")
    for elem in liste:
        print(f"elem = {elem}")
    print("--------------------------------------")
    liste = myBook.get_recipes_by_types("toto")
    print("--------------------------------------")
    print(myBook.get_recipe_by_name("pizza"))
    print("--------------------------------------")
    myBook.get_recipe_by_name("salad")
    print("--------------------------------------")
    myBook.get_recipe_by_name("salades")
    print("--------------------------------------")
    sys_exit()
