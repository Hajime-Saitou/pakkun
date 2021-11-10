import bpy
from .Origin import Origin
from .Iterator import Iterator
from .NodeLink import NodeLink

class NodeLinks(Iterator):
    def __init__(self, nodeLinks, origin):
        super().__init__()

        self.nodeLinks = nodeLinks
        self.origin = origin

        self.__setProperty(nodeLinks)

    def __setProperty(self, nodeLinks):
        pass

    def __getitem__(self, key):
        if self.find(key) < 0:
            raise KeyError(f"Undefined node key '{key}'.")

        return NodeLink(self.nodeLinks[key], self.origin)

    @property
    def length(self):
        return len(self.nodeLinks) if self.nodeLinks is not None else 0

    def find(self, key) -> int:
        if self.nodeLinks is None:
            return -2

        if type(key) is int:
            return key if 0 <= key < self.length else -1
        else:
            return self.nodeLinks.find(key)

    @property
    def serialize(self):
        properties = {}

        properties["nodeLinks"] = [ NodeLink(nodeLink, self.origin).serialize for nodeLink in self.nodeLinks ]

        return properties
