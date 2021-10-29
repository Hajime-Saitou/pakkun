import bpy
from mathutils import Vector
from .Origin import Origin

class ShapeKey(object):
    def __init__(self, shapeKey, origin):
        self.shapeKey = shapeKey
        self.origin = origin

        self.__setProperty(shapeKey)

    def __setProperty(self, shapeKey):
        self.name:str = shapeKey.name
        self.index:int = shapeKey.id_data.key_blocks.find(self.name)
        self.frame:float = shapeKey.frame
        self.mute:bool = shapeKey.mute
        self.relativeKeyName:str = shapeKey.relative_key.name
        self.sliderMin:float = shapeKey.slider_min
        self.sliderMax:float = shapeKey.slider_max
        self.value:float = shapeKey.value
        self.vertexGroupName:str = shapeKey.vertex_group

    @property
    def co(self) -> list:
        return [ data.co for data in self.shapeKey.data ]

    @property
    def serialize(self) -> dict:
        properties = {}
        properties["name"] = self.name
        properties["co"] = [ tuple(co) for co in self.co ]
        properties["mute"] = self.mute
        properties["relativeKeyName"] = self.relativeKeyName
        properties["sliderMin"] = self.sliderMin
        properties["sliderMax"] = self.sliderMax
        properties["value"] = self.value
        properties["vertexGroupName"] = self.vertexGroupName

        return properties

    def deserialize(self, properties:dict):
        for index, co in enumerate([ Vector(co) for co in properties["co"] ]):
            self.shapeKey.data[index].co = co
        self.shapeKey.mute = properties["mute"]

        relativeTo = self.shapeKey.id_data.key_blocks.find(properties["relativeKeyName"])
        if relativeTo < 0:
            relative_key = self.origin.origin.shape_key_add(name=properties["relativeKeyName"])
        else:
            relative_key = self.shapeKey.id_data.key_blocks[properties["relativeKeyName"]]
        self.shapeKey.relative_key = relative_key

        self.shapeKey.slider_min = properties["sliderMin"]
        self.shapeKey.slider_max = properties["sliderMax"]
        self.shapeKey.value = properties["value"]
        self.shapeKey.vertex_group = properties["vertexGroupName"]
