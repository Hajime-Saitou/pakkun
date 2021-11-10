import bpy
from .Origin import Origin
from .Nodes import Nodes

class NodeTree(object):
    def __init__(self, nodeTree, origin):
        self.nodeTree = nodeTree
        self.origin = origin

        self.__setProperty(nodeTree)

    def __setProperty(self, nodeTree):
        if nodeTree is None:
            return

    @property
    def nodes(self):
        return Nodes(self.nodeTree.nodes, self.origin) if self.nodeTree else None

    @property
    def links(self):
        return NodeLinks(self.nodeTree.links, self.origin) if self.nodeTree else None

    @property
    def serialize(self) -> dict:
        properties = {}

        properties["activeInput"] = self.nodeTree.active_input
        properties["activeOutput"] = self.nodeTree.active_output
        properties["links"] = self.links.serialize
        properties["name"] = self.nodeTree.name
        properties["nodes"] = self.nodes.serialize
        properties["tag"] = self.nodeTree.tag
        properties["useFakeUser"] = self.nodeTree.use_fake_user
        properties["viewCenter"] = tuple(self.nodeTree.view_center)

        return properties
