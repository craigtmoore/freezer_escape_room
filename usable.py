from abc import ABC


class Usable(ABC):

    def __init__(self):
        self.name = ''
        self.description = ''

    def can_pickup(cls) -> bool:
        return True
