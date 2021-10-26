import bpy
from .Origin import Origin
from .Vertices import Vertices

class Face(object):
    def __init__(self, face, origin):
        self.face = face
        self.origin = origin

        self.__setProperty(face)

    def __setProperty(self, face):
        self.index = face.index

    @property
    def vertices(self):
        return Vertices([ self.origin.origin.data.vertices[index] for index in self.face.vertices ], Origin(self.origin.origin, self))

    @property
    def loopIndices(self):
        return [ index for index in self.face.loop_indices ]

    def toLoopIndex(self, vertexIndex:int):
        return self.loopIndices[[ index for index in self.face.vertices ].index(vertexIndex)]

    @property
    def materialIndex(self):
        return self.face.material_index
