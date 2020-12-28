from typing import Set

from inspectable import Inspectable


class Closet(Inspectable):

    def __init__(self):
        super().__init__()
        self.name = "closet"
        self.description = "A closet with two doors"
        self.inspected = False

    def inspect(self) -> Set:
        if not self.inspected:
            print('You open the closet doors and find a hat, gloves, and warm coat.')
            print('You eagerly put on all the close in order to warm up.')
            self.inspected = True
        else:
            print('You open the close doors and find it is empty.')

        return set()
