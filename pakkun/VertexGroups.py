from .VertexGroup import VertexGroup

class VertexGroups(object):
    def __init__(self, object):
        self.object = object

    def __getitem__(self, key):
        return VertexGroup(self.object, key)
