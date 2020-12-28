from typing import Set

from inspectable import Inspectable
from interactable import Interactable
from items import Flashlight, Hammer, TapePlayer


class Shelf(Inspectable):

    def __init__(self):
        super().__init__()
        self.name = "shelf"
        self.description = "A shelf with an assortment of items on it."
        self.items = [TapePlayer(), Flashlight(), Hammer()]

    def inspect(self) -> Set:
        found_items = set()
        for item in self.items:

            if isinstance(item, Inspectable):
                item.inspect()
            else:
                print(f"You find a {item.description}")

            if item.can_pickup():
                print("  - this might be useful so you pick it up")
                found_items.add(item)

            if isinstance(item, Interactable):
                found_items.add(item)

        for item in found_items:
            if item.can_pickup():
                self.items.remove(item)

        return found_items
