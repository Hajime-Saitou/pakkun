import bpy
from .Origin import Origin
from .Material import Material

class MaterialSlot(object):
    def __init__(self, materialSlot, origin):
        self.materialSlot = materialSlot
        self.origin = origin

        self.__setProperty(materialSlot)

    def __setProperty(self, materialSlot):
        pass

    @property
    def material(self):
        return Material(self.materialSlot.material, self.origin)

    @property
    def isEmpty(self) -> bool:
        return self.materialSlot.material is None

    @property
    def serialize(self) -> dict:
        properties = {}
        properties["name"] = self.materialSlot.name
        properties["material"] = self.material.serialize if not self.isEmpty else {}
        properties["link"] = self.materialSlot.link
        
        return properties
