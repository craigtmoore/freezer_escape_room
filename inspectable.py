from abc import ABC, abstractmethod
from typing import Set


class Inspectable(ABC):

    def __init__(self):
        self.name = ''
        self.description = ''

    @abstractmethod
    def inspect(self) -> Set:
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
