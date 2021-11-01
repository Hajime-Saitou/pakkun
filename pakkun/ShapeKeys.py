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
        if shapeKeys is None:
            return

        self.name = shapeKeys.name
        self.evalTime = shapeKeys.eval_time
        self.tag = shapeKeys.tag
        self.useFakeUser = shapeKeys.use_fake_user
        self.useRelative = shapeKeys.use_relative

    @property
    def keyBlocks(self):
        return None if self.origin.origin.data.shape_keys is None else self.origin.origin.data.shape_keys.key_blocks

    def __getitem__(self, key):
        if self.find(key) < 0:
            raise KeyError(f"Undefined shape key block '{key}'.")

        return ShapeKey(self.keyBlocks[key], self.origin)

    @property
    def length(self):
        return len(self.keyBlocks) if self.keyBlocks is not None else 0

    @property
    def indeces(self) -> list:
        return [ shapeKey.index for shapeKey in self ]

    def find(self, key) -> int:
        if self.keyBlocks is None:
            return -2

        if type(key) is int:
            return key if 0 <= key < self.length else -1
        else:
            return self.keyBlocks.find(key)

    def add(self, name:str, fromMix:bool=False, unique:bool=False):
        if unique and self.find(name) >= 0:
            shapeKeyBlock = self.origin.origin.data.shape_keys.key_blocks[name]
        else:
            shapeKeyBlock = self.origin.origin.shape_key_add(name=name, from_mix=fromMix)

        return ShapeKey(shapeKeyBlock, self.origin)

    def clear(self):
        self.origin.origin.shape_key_clear()

    @property
    def serialize(self):
        properties = {}

        properties["name"] = self.shapeKeys.name
        properties["evalTime"] = self.shapeKeys.eval_time
        properties["tag"] = self.shapeKeys.tag
        properties["useFakeUser"] = self.shapeKeys.use_fake_user
        properties["useRelative"] = self.shapeKeys.use_relative
        
        properties["keyBlocks"] = [ shapeKey.serialize for shapeKey in self ]

        return properties

    def mergeKeyBlocks(self, properties:dict, unique:bool=False):
        nameOrder = [ shapeKey.name for shapeKey in self ]

        for keyBlockProperty in properties:
            shapeKey = self.add(keyBlockProperty["name"], unique=unique)
            shapeKey.deserialize(keyBlockProperty)
            if shapeKey.name not in nameOrder:
                nameOrder.append(shapeKey.name)         # using new name

        self.sort(nameOrder)

    def deserialize(self, properties:dict):
        self.clear()

        self.mergeKeyBlocks(properties["keyBlocks"], unique=True)

        self.shapeKeys = self.origin.origin.data.shape_keys
        self.shapeKeys.name = properties["name"]
        self.shapeKeys.eval_time = properties["evalTime"]
        self.shapeKeys.tag = properties["tag"]
        self.shapeKeys.use_fake_user = properties["useFakeUser"]
        self.shapeKeys.use_relative = properties["useRelative"]

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
