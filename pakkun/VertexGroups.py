from .Iterator import Iterator
from .Origin import Origin
from .VertexGroup import VertexGroup

class VertexGroups(Iterator):
    def __init__(self, vertexGroups, origin):
        super().__init__()

        self.vertexGroups = vertexGroups
        self.origin = origin

    def __getitem__(self, key):
        if self.find(key) == -1:
            raise KeyError(f"Undefined vertex group '{key}'.")

        return VertexGroup(self.vertexGroups[key], self.origin)

    @property
    def length(self) -> int:
        return len(self.vertexGroups)

    def find(self, key) -> int:
        if type(key) is int:
            return key if 0 <= key < self.length else -1
        else:
            return self.vertexGroups.find(key)
