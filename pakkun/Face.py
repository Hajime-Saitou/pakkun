from .Origin import Origin
from .Vertices import Vertices

class Face(object):
    def __init__(self, object, key:int):
        self.object = object
        self.name = str(key)
        self.origin = Origin(self.object, self)
        self.face = self.object.data.polygons[key]

    @property
    def vertices(self):
        vertices = [ self.object.data.vertices[index] for index in self.face.vertices ]
        return Vertices(vertices, origin=self.origin)

    @property
    def loopIndices(self):
        return [ index for index in self.face.loop_indices ]

    def toLoopIndex(self, vertexIndex:int):
        print(vertexIndex)
        return self.loopIndices[[ index for index in self.face.vertices ].index(vertexIndex)]
