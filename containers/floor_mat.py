from typing import Set

from inspectable import Inspectable
from items import Paper


class FloorMat(Inspectable):

    def __init__(self):
        super().__init__()
        self.name = 'floor mat'
        self.description = 'A floor mat'

    def inspect(self) -> Set:
        print('You look down to see a dirty floor mat.')
        print('You lift up one corner and see a blank piece of paper lying on the floor')
        return {Paper()}
