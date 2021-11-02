class NodeIos(object):
    def __init__(self, ios):
        self.ios = ios
        self.__setProperty(ios)

    def __setProperty(self, ios):
        self.name:str = ios.name

    @property
    def defaultValue(self) -> any:
        return self.ios.default_value

    @property
    def serializable(self) -> bool:
        print(self.ios.type)
        return self.ios.type in [ "VALUE", "VECTOR", "RGBA" ]

    @property
    def serializableDefaultValue(self) -> any:
        if self.ios.type == "VALUE":
            return self.defaultValue
        elif self.ios.type in [ "VECTOR", "RGBA" ]:
            return tuple(self.defaultValue)

        raise BlenderTypeError(f"Undefined node input/output type {self.ios.type}.")

    @property
    def serialize(self) -> dict:
        properties = {}

        properties["name"] = self.ios.name
        properties["defaultValue"] = self.serializableDefaultValue
        properties["enabled"] = self.ios.enabled
        properties["hide"] = self.ios.hide
        properties["hideValue"] = self.ios.hide_value
        properties["label"] = self.ios.label
        properties["showExpanded"] = self.ios.show_expanded
        properties["type"] = self.ios.type

        return properties
