import bpy
from .Origin import Origin
from .Iterator import Iterator
from .ShapeKey import ShapeKey

class ShapeKeys(Iterator):
    def __init__(self, shapeKeys, origin):
        super().__init__()

        self.shapeKeys = shapeKeys
        self.origin = origin

        self.__setProperty(shapeKeys)

    def __setProperty(self, shapeKeys):
        if self.origin.origin.data.shape_keys is None:
            self.keyBlocks = None
        else:
            self.keyBlocks = shapeKeys.key_blocks

    def __getitem__(self, key):
        if self.find(key) < 0:
            raise KeyError(f"Undefined shape key block '{key}'.")

        return ShapeKey(self.keyBlocks[key], self.origin)

    @property
    def length(self):
        return len(self.keyBlocks)

    def find(self, key) -> int:
        if self.keyBlocks is None:
            return -2

        if type(key) is int:
            return key if 0 <= key < self.length else -1
        else:
            return self.keyBlocks.find(key)

    def add(self, name:str, fromMix:bool=False, unique=False):
        if self.find(name) < 0:
            shapeKeyBlock = self.origin.origin.shape_key_add(name=name, from_mix=fromMix)
        else:
            shapeKeyBlock = self.origin.origin.data.shape_keys.key_blocks[name]

        return ShapeKey(shapeKeyBlock, self.origin)

    def clear(self):
        self.origin.origin.shape_key_clear()

    @property
    def serialize(self):
        properties = {}

    def activate(self, key) -> bool:
        shapeKeyIndex = self.find(key)
        if shapeKeyIndex < 0:
            return False

        self.origin.origin.active_shape_key_index = shapeKeyIndex
        return True

    def sort(self, keys):
        if len(keys) != self.length:
            ValueError("Illegal key length.")
        
        for key in keys:
            self.activate(key)
            bpy.ops.object.shape_key_move(type="BOTTOM")
