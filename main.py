from typing import List

from containers.chest import Chest
from containers.circuit_breaker import CircuitBreakerPanel
from containers.closet import Closet
from containers.door import Door
from containers.door_button import DoorButton
from containers.floor_mat import FloorMat
from containers.ice_block import IceBlock
from containers.shelf import Shelf
from inspectable import Inspectable
from interactable import Interactable
from items import Batteries, Flashlight, TapePlayer, Tape
from usable import Usable


class Main():

    def __init__(self):
        panel = CircuitBreakerPanel()
        self.left_containers = [panel, IceBlock(), Closet()]
        self.forward_containers = [Door(), DoorButton(panel)]
        self.right_containers = [Chest(), Shelf()]
        self.down_containers = [FloorMat()]
        self.up_containers = []
        self.inspectable_objects = []
        self.interactable_objects = []
        self.inventory = []

    @staticmethod
    def get_main_options():
        option = ''
        valid_options = ['I', 'U', 'L']
        while not option:
            option = input(f"you have {len(valid_options)} options [I]nspect, [L]ook, or [U]se: ").upper()
            if option not in valid_options:
                print(f"'{option}' is not a valid option")
                option = ''

        return option

    def get_look_option(self):
        option = ''
        valid_options = ['F', 'U', 'D', 'R', 'L']
        while not option:
            print("You have 5 options")
            print(" - look [F]orward")
            print(" - look [U]p")
            print(" - look [D]own")
            print(" - look [R]ight")
            print(" - look [L]eft")
            option = input("What option do you choose? ").upper()
            if option not in valid_options:
                print(f"'{option}' is not a valid option")

        return option

    def get_inspectable_object(self) -> Inspectable:
        option = -1
        num_objects = len(self.inspectable_objects)
        while option == -1:
            print(f"You have {num_objects} options")
            for i, object in enumerate(self.inspectable_objects):
                print(f" - [{i}] {object.description}")
            option = self.get_numeric_option(num_objects - 1)

        return self.inspectable_objects[option]

    @staticmethod
    def get_numeric_option(max_value):
        option = input("What option do you choose? ")
        if option.isnumeric():
            option = int(option)
            if not (0 <= option <= max_value):
                print(f"'{option}' is not a valid option")
                option = -1
        else:
            print(f"'{option}' is not a valid option")
            option = -1
        return option

    def get_inventory_object(self) -> Usable:
        option = -1
        num_objects = len(self.inventory)
        while option == -1:
            print(f"You have {num_objects} usable objects")
            for i, object in enumerate(self.inventory):
                print(f" - [{i}] {object.description}")
            option = self.get_numeric_option(num_objects - 1)

        return self.inventory[option]

    def get_interactable_object(self) -> Interactable:

        option = -1
        num_objects = len(self.interactable_objects)
        while option == -1:
            print(f"You use it on one of these {num_objects} objects")
            for i, interactable in enumerate(self.interactable_objects):
                print(f" - [{i}] {interactable.description}")
            option = self.get_numeric_option(num_objects - 1)

        return self.interactable_objects[option]

    def run(self):
        print("You awake lying on the floor and shivering. You seem to be in some sort of freezer")
        finished = False
        while not finished:

            option = self.get_main_options()

            if option == 'L':
                option = self.get_look_option()
                if option == 'F':
                    self.print_containers('forward', self.forward_containers)
                if option == 'R':
                    self.print_containers('right', self.right_containers)
                if option == 'L':
                    self.print_containers('left', self.left_containers)
                if option == 'U':
                    self.print_containers('up', self.up_containers)
                if option == 'D':
                    self.print_containers('down', self.down_containers)

            if option == 'I':

                if not self.inspectable_objects:
                    print("You should look around, you haven't discovered anything to inspect yet.")
                else:
                    inspectable = self.get_inspectable_object()

                    if inspectable is not None:
                        if isinstance(inspectable, DoorButton):
                            finished = inspectable.press()
                        else:

                            items = inspectable.inspect()

                            self.add_items(items)

            if option == 'U':

                if not self.inventory:
                    print("You have nothing in your inventory to use.")
                else:
                    item = self.get_inventory_object()
                    print(f"What do you want to use the {item.name} on? ")
                    interactable = self.get_interactable_object()

                    items = interactable.interact(item)

                    if isinstance(item, Batteries) and isinstance(interactable, Flashlight):
                        self.inventory.remove(item)

                    if isinstance(item, Tape) and isinstance(interactable, TapePlayer):
                        self.inventory.remove(item)

                    self.add_items(items)

        print("Thanks for playing!")

    def add_items(self, items):
        for item in items:

            if isinstance(item, Usable) and item.can_pickup():
                self.add(self.inventory, item)

            if isinstance(item, Inspectable):
                self.add(self.inspectable_objects, item)

            if isinstance(item, Interactable):
                self.add(self.interactable_objects, item)

    def print_containers(self, direction: str, containers: List[Inspectable]):
        print(f'You look {direction} and see')

        if not containers:
            print('  - nothing obvious')

        for container in containers:
            self.add(self.inspectable_objects, container)
            print(f" - {container.description}")
            if isinstance(container, Interactable):
                self.add(self.interactable_objects, container)

    def add(self, list: List, item):

        in_list = False

        for entry in list:
            if item == entry:
                in_list = True

        if not in_list:
            list.append(item)


if __name__ == '__main__':
    Main().run()
