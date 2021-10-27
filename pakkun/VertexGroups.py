from .Iterator import Iterator
from .Origin import Origin
from .VertexGroup import VertexGroup

class VertexGroups(Iterator):
    def __init__(self, vertexGroups, origin):
        super().__init__()

        self.vertexGroups = vertexGroups
        self.origin = origin

    def __getitem__(self, key):
        if self.vertexGroups.find(key) == -1:
            raise KeyError(f"Undefined vertex group '{key}''.")

        return VertexGroup(self.vertexGroups[key], self.origin)

    @property
    def length(self):
        return len(self.vertexGroups)
