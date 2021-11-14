import bpy
from .Origin import Origin

class NodeLink(object):
    def __init__(self, link, origin):
        self.link = link
        self.origin = origin

        self.__setProperty(link)

    def __setProperty(self, link):
        pass

    @property
    def serialize(self):
        properties = {}

        properties["fromNodeName"] = self.link.from_node.name
        properties["fromSocketIndex"] = [ socket.as_pointer() for socket in self.link.from_node.outputs ].index(self.link.from_socket.as_pointer())
        properties["fromSocketName"] = self.link.from_socket.name
        properties["isHidden"] = self.link.is_hidden
        properties["isMuted"] = self.link.is_muted
        properties["isValid"] = self.link.is_valid
        properties["toNodeName"] = self.link.to_node.name
        properties["toSocketIndex"] = [ socket.as_pointer() for socket in self.link.to_node.inputs ].index(self.link.to_socket.as_pointer())
        properties["toSocketName"] = self.link.to_socket.name

        return properties