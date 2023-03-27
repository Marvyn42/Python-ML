class GotCharacter:
    """Create a character"""

    def __init__(self, first_name=None, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self) -> str:
        if self.first_name:
            txt = f"My name is {self.first_name} and i'm "
        else:
            txt = "I am nameless and i'm "
        txt += "alive." if self.is_alive is True else txt == txt + "not alive."
        return txt


class Stark(GotCharacter):
    """Create a Stark's house character"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
