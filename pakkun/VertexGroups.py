from .VertexGroup import VertexGroup
from .Iterator import Iterator

class VertexGroups(Iterator):
    def __init__(self, object):
        super().__init__()

        self.object = object

    def __getitem__(self, key):
        if self.object.vertex_groups.find(key) == -1:
            raise KeyError(f"Undefined vertex group '{key}''.")

        return VertexGroup(self.object, key)

    @property
    def length(self):
        return len(self.object.vertex_groups)
