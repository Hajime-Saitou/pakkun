import bpy
from .Origin import Origin
from .Iterator import Iterator
from .Node import Node

class Nodes(Iterator):
    def __init__(self, nodes, origin):
        super().__init__()

        self.nodes = nodes
        self.origin = origin

        self.__setProperty(nodes)

    def __setProperty(self, nodes):
        if nodes is None:
            return

    def __getitem__(self, key):
        if self.find(key) < 0:
            raise KeyError(f"Undefined node key '{key}'.")

        return Node(self.nodes[key], self.origin)

    @property
    def length(self):
        return len(self.nodes) if self.nodes is not None else 0

    def find(self, key) -> int:
        if self.nodes is None:
            return -2

        if type(key) is int:
            return key if 0 <= key < self.length else -1
        else:
            return self.nodes.find(key)

    def clear(self):
        self.nodes.clear()

    @property
    def serialize(self):
        properties = {}

        properties["active"] = self.nodes.active.name
        properties["nodes"] = [ Node(node, self.origin).serialize for node in self.nodes ]

        return properties

    def danglingNodes(self):
        return Nodes([ node for node in self.nodes if Node(node, None).dangled ], self.origin)

    def linkedErrorNodes(self):
        return Nodes([ node for node in self.nodes if Node(node, None).linkedError ], self.origin)

    def containingCategory(self, category:str):
        return Nodes([ node for node in self.nodes if Node(node, None).category == category ], self.origin)
