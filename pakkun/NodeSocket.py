from .Exception.BlenderTypeError import BlenderTypeError

class NodeSocket(object):
    def __init__(self, socket):
        self.socket = socket
        self.__setProperty(socket)

    def __setProperty(self, socket):
        self.name:str = socket.name

    @property
    def defaultValue(self) -> any:
        return self.socket.default_value

    @property
    def serializable(self) -> bool:
        print(self.socket.type)
        return self.socket.type in [ "BOOLEAN", "COLLECTION", "CUSTOM", "GEOMETRY", "IMAGE", "INT", "OBJECT", "RGBA", "SHADER", "STRING", "VALUE", "VECTOR", ]

    @property
    def serializableDefaultValue(self) -> any:
        if self.socket.type in [ "BOOLEAN", "INT", "STRING", "VALUE", ]:
            return self.defaultValue
        elif self.socket.type in [ "RGBA", "VECTOR", ]:
            return tuple(self.defaultValue)
        else:
            return self.socket.type

        raise BlenderTypeError(f"Undefined node input/output type {self.socket.type}.")

    @property
    def serialize(self) -> dict:
        properties = {}

        properties["name"] = self.socket.name
        if self.socket.type != "CUSTOM":
            properties["defaultValue"] = self.serializableDefaultValue
        properties["enabled"] = self.socket.enabled
        properties["hide"] = self.socket.hide
        properties["hideValue"] = self.socket.hide_value
        properties["label"] = self.socket.label
        properties["showExpanded"] = self.socket.show_expanded
        properties["type"] = self.socket.type

        return properties
