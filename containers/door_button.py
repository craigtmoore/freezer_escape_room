from typing import Set, List

from containers.circuit_breaker import CircuitBreakerPanel
from inspectable import Inspectable
from interactable import Interactable
from usable import Usable


class DoorButton(Interactable, Inspectable):

    def __init__(self, circuit_breaker: CircuitBreakerPanel):
        super().__init__()
        self.name = "button"
        self.description = "a button for opening the door"
        self.circuit_breaker = circuit_breaker

    def interact(self, usable: Usable) -> List:
        self.press()
        return []

    def press(self) -> bool:
        print("You press the button...")

        if self.circuit_breaker.is_powered:
            print("  You hear a motor activate, and the door opens. You escape to freedom.")
            return True

        print("  Nothing happens, it seems there is no power.")
        return False

    def inspect(self) -> Set:
        print("You see a button next to the door.")
        self.press()
        return set()
