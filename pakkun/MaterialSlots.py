import bpy
from .Origin import Origin
from .Iterator import Iterator
from .NodeLink import NodeLink
from .MaterialSlot import MaterialSlot

class MaterialSlots(Iterator):
    def __init__(self, materialSlots, origin):
        super().__init__()

        self.materialSlots = materialSlots
        self.origin = origin

        self.__setProperty(materialSlots)

    def __setProperty(self, materialSlots):
        pass

    def __getitem__(self, key):
        if self.find(key) < 0:
            raise KeyError(f"Undefined material key '{key}'.")

        return MaterialSlot(self.materialSlots[key], self.origin)

    @property
    def length(self):
        return len(self.materialSlots) if self.materialSlots is not None else 0

    def find(self, key) -> int:
        if self.materialSlots is None:
            return -2

        if type(key) is int:
            return key if 0 <= key < self.length else -1
        else:
            return self.materialSlots.find(key)

    @property
    def serialize(self):
        properties = {}
        properties["materialSlots"] = [ MaterialSlot(materialSlot, self.origin).serialize for materialSlot in self.materialSlots  ]
        return properties
