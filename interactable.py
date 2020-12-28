from abc import ABC
from typing import List

from usable import Usable


class Interactable(ABC):

    def __init__(self):
        self.name = ''
        self.description = ''

    def interact(self, usable: Usable) -> List:
        pass
